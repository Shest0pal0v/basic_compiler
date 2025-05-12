from basic_compiler.ast.nodes import *

class SemanticError(Exception):
    pass

class SemanticAnalyzer:
    def __init__(self):
        self.scopes = [{}]

    def declare(self, name: str, t: str):
        scope = self.scopes[-1]
        if name in scope:

            return
        scope[name] = t

    def lookup(self, name: str):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise SemanticError(f"Use of undeclared '{name}'")

    def check(self, node: Node):
        fn = getattr(self, f"check_{type(node).__name__}", self.generic_check)
        return fn(node)

    def generic_check(self, node: Node):
        for c in node.children():
            self.check(c)

    def check_Program(self, p: Program):
        for st in p.statements:
            self.check(st)

    def check_Assign(self, a: Assign):
        t = self.check(a.value)

        self.declare(a.name, t)
        return t

    def check_Var(self, v: Var):
        return self.lookup(v.name)

    def check_Number(self, n: Number):
        return 'float' if isinstance(n.value, float) else 'int'

    def check_String(self, s: String):
        return 'string'

    def check_BinOp(self, b: BinOp):
        lt = self.check(b.left)
        rt = self.check(b.right)
        if b.op in ('+','-','*','/'):
            if lt not in ('int','float') or rt not in ('int','float'):
                raise SemanticError(f"Operator {b.op} not supported for {lt},{rt}")
            return 'float' if 'float' in (lt, rt) else 'int'

        return 'bool'

    def check_Print(self, p: Print):
        self.check(p.expr)

    def check_If(self, i: If):
        if self.check(i.condition) != 'bool':
            raise SemanticError("IF condition must be bool")
        for st in i.then_branch:
            self.check(st)
        for st in i.else_branch:
            self.check(st)

    def check_For(self, f: For):
        st = self.check(f.start)
        ed = self.check(f.end)
        if st not in ('int','float') or ed not in ('int','float'):
            raise SemanticError("FOR bounds must be numeric")

        self.declare(f.var.name, st)
        if f.step:
            if self.check(f.step) not in ('int','float'):
                raise SemanticError("FOR step must be numeric")

    def check_Next(self, n: Next):

        self.lookup(n.var)

    def check_While(self, w: While):
        if self.check(w.condition) != 'bool':
            raise SemanticError("WHILE condition must be bool")
        for st in w.body:
            self.check(st)

    def check_Goto(self, g: Goto):
        pass

    def check_Gosub(self, g: Gosub):
        pass

    def check_Return(self, r: Return):
        pass

    def check_Read(self, r: Read):
        for v in r.vars:
            if isinstance(v, Var):

                self.declare(v.name, 'string')
            elif isinstance(v, ArrayRef):

                self.lookup(v.array.name)

    def check_Input(self, inp: Input):
        for v in inp.vars:
            if isinstance(v, Var):
                self.declare(v.name, 'string')
            elif isinstance(v, ArrayRef):
                self.lookup(v.array.name)

    def check_Dim(self, d: Dim):
        for v in d.vars:
            if isinstance(v, Var):
                self.declare(v.name, 'array')
            elif isinstance(v, ArrayRef):

                self.declare(v.array.name, 'array')

    def check_Data(self, d: Data):
        for val in d.values:
            self.check(val)

    def check_End(self, e: End):
        pass
