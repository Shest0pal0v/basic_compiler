from basic_compiler.ast.nodes import *

class CodeGenerator:
    def __init__(self):
        self.code = []
        self.indent = 0
        self.label_funcs = []
        self.statements = []
        self.gosub_stack_used = False

    def emit(self, line):
        self.code.append("    " * self.indent + line)

    def generate(self, node: Node):
        if isinstance(node, Program):
            self.statements = node.statements
        self.collect_labels()
        self.emit("# Generated Python code from BASIC")
        if self.gosub_stack_used:
            self.emit("_gosub_stack = []")
        self.emit("")
        self.emit("def main():")
        self.indent += 1
        self.emit(f"return label_{self.label_funcs[0]}()")
        self.indent -= 1
        self.emit("")
        self.emit("if __name__ == '__main__':")
        self.indent += 1
        self.emit("main()")
        self.indent -= 1
        self.emit("")
        for stmt in self.statements:
            self.gen_stmt(stmt)

    def collect_labels(self):
        for stmt in self.statements:
            if isinstance(stmt, Label):
                self.label_funcs.append(stmt.name)

    def gen_stmt(self, stmt):
        method = getattr(self, f"gen_{type(stmt).__name__}", self.gen_default)
        method(stmt)

    def gen_default(self, node):
        raise NotImplementedError(f"No generator for {type(node).__name__}")

    def gen_Label(self, label: Label):
        self.emit(f"\ndef label_{label.name}():")
        self.indent += 1

    def gen_Assign(self, a: Assign):
        name = self.sanitize_name(a.name)
        self.emit(f"{name} = {self.expr(a.value)}")

    def gen_Print(self, p: Print):
        self.emit(f"print({self.expr(p.expr)})")

    def gen_If(self, node: If):
        cond = self.expr(node.condition)
        self.emit(f"if {cond}:")
        self.indent += 1
        for stmt in node.then_branch:
            self.gen_stmt(stmt)
        self.indent -= 1
        if node.else_branch:
            self.emit("else:")
            self.indent += 1
            for stmt in node.else_branch:
                self.gen_stmt(stmt)
            self.indent -= 1

    def gen_Goto(self, node: Goto):
        self.emit(f"return label_{node.target}()")

    def gen_Gosub(self, node: Gosub):
        self.gosub_stack_used = True
        return_id = f"return_point_{len(self.code)}"
        self.emit(f"def {return_id}():")
        self.indent += 1
        self.emit("return None  # Placeholder return point")
        self.indent -= 1
        self.emit(f"_gosub_stack.append({return_id})")
        self.emit(f"return label_{node.target}()")

    def gen_Return(self, node: Return):
        self.emit("return _gosub_stack.pop()()")

    def gen_For(self, node: For):
        var = self.sanitize_name(node.var.name)
        start = self.expr(node.start)
        end = self.expr(node.end)
        step = self.expr(node.step) if node.step else "1"
        self.emit(f"for {var} in range(int({start}), int({end}) + 1, int({step})):")  # inclusive
        self.indent += 1

    def gen_Next(self, node: Next):
        self.indent -= 1

    def gen_While(self, node: While):
        self.emit(f"while {self.expr(node.condition)}:")
        self.indent += 1
        for stmt in node.body:
            self.gen_stmt(stmt)
        self.indent -= 1

    def gen_Read(self, node: Read):
        for var in node.vars:
            self.emit(f"{self.expr(var)} = data.pop(0)")

    def gen_Input(self, node: Input):
        prompt = repr(node.prompt) if node.prompt else '"?"'
        for v in node.vars:
            name = self.sanitize_name(v.name)
            self.emit(f"{name} = input({prompt})")

    def gen_Dim(self, node: Dim):
        for arr in node.vars:
            if isinstance(arr, ArrayRef):
                size = self.expr(arr.index)
                self.emit(f"{arr.array.name} = [0] * (int({size}) + 1)")

    def gen_Data(self, node: Data):
        values = ", ".join(self.expr(v) for v in node.values)
        self.emit(f"data = [{values}]")

    def gen_End(self, node: End):
        self.emit("exit()")

    def expr(self, node: Node):
        if isinstance(node, Number):
            return str(node.value)
        elif isinstance(node, String):
            return repr(node.value)
        elif isinstance(node, Var):
            return self.sanitize_name(node.name)
        elif isinstance(node, BinOp):
            op = node.op
            if op == '=':
                op = '=='
            return f"({self.expr(node.left)} {op} {self.expr(node.right)})"
        elif isinstance(node, ArrayRef):
            return f"{node.array.name}[{self.expr(node.index)}]"
        elif isinstance(node, FuncCall):
            return f"{node.name.lower()}({', '.join(self.expr(a) for a in node.args)})"
        else:
            raise NotImplementedError(f"Unknown expression: {type(node).__name__}")

    def sanitize_name(self, name: str):
        return name.replace('%', '_int').replace('$', '_str').replace('!', '_flt')

    def get_code(self):
        return "\n".join(self.code)
