from basic_compiler.ast.nodes import *

class Optimizer:
    def optimize(self, node: Node) -> Node:
        method = getattr(self, f"opt_{type(node).__name__}", self.default)
        return method(node)

    def default(self, node: Node) -> Node:
        for field in node.children():
            self.optimize(field)
        return node

    def opt_BinOp(self, b: BinOp) -> Node:
        b.left = self.optimize(b.left)
        b.right = self.optimize(b.right)


        if isinstance(b.left, Number) and isinstance(b.right, Number):
            try:
                result = eval(f"{b.left.value} {b.op} {b.right.value}")
                return Number(str(result))
            except:
                pass


        if b.op == '*' and (isinstance(b.left, Number) and b.left.value == 0 or isinstance(b.right, Number) and b.right.value == 0):
            return Number("0")
        if b.op == '+' and isinstance(b.right, Number) and b.right.value == 0:
            return b.left
        if b.op == '+' and isinstance(b.left, Number) and b.left.value == 0:
            return b.right
        return b

    def opt_Assign(self, a: Assign):
        a.value = self.optimize(a.value)
        return a

    def opt_Print(self, p: Print):
        p.expr = self.optimize(p.expr)
        return p

    def opt_If(self, i: If):
        i.condition = self.optimize(i.condition)
        i.then_branch = [self.optimize(stmt) for stmt in i.then_branch]
        i.else_branch = [self.optimize(stmt) for stmt in i.else_branch] if i.else_branch else []
        return i

    def opt_Program(self, p: Program):
        p.statements = [self.optimize(st) for st in p.statements]
        return p
    def opt_While(self, w: While):
        w.condition = self.optimize(w.condition)
        w.body = [self.optimize(stmt) for stmt in w.body if stmt]
        return w

    def opt_For(self, f: For):
        f.var = self.optimize(f.var)
        f.start = self.optimize(f.start)
        f.end = self.optimize(f.end)
        if f.step:
            f.step = self.optimize(f.step)
        return f

    def opt_Read(self, r: Read):
        r.vars = [self.optimize(v) for v in r.vars]
        return r

    def opt_Input(self, inp: Input):
        inp.vars = [self.optimize(v) for v in inp.vars]
        return inp

    def opt_End(self, e: End):
        return e

    def opt_Program(self, p: Program):
        p.statements = [self.optimize(st) for st in p.statements if st is not None]
        return p

