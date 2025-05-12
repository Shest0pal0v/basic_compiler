from typing import List

class Node:
    def to_string(self) -> str:
        raise NotImplementedError
    def children(self) -> List['Node']:
        return []

class Program(Node):
    def __init__(self, statements: List[Node]):
        self.statements = statements
    def to_string(self): return "Program"
    def children(self):  return self.statements

class Label(Node):
    def __init__(self, name):
        self.name = name

    def children(self):
        return []

    def to_string(self):
        return f"Label({self.name})"

class Assign(Node):
    def __init__(self, name: str, value: Node):
        self.name, self.value = name, value
    def to_string(self): return f"Assign({self.name})"
    def children(self):  return [self.value]

class Print(Node):
    def __init__(self, expr: Node):
        self.expr = expr
    def to_string(self): return "Print"
    def children(self):  return [self.expr]

class If(Node):
    def __init__(self, condition: Node, then_branch: List[Node], else_branch: List[Node]):
        self.condition, self.then_branch, self.else_branch = condition, then_branch, else_branch
    def to_string(self): return "If"
    def children(self):  return [self.condition] + self.then_branch + self.else_branch

class For(Node):
    def __init__(self, var: Node, start: Node, end: Node, step: Node = None):
        self.var, self.start, self.end, self.step = var, start, end, step
    def to_string(self): return f"For({self.var.name})"
    def children(self):
        kids = [self.var, self.start, self.end]
        if self.step: kids.append(self.step)
        return kids

class Next(Node):
    def __init__(self, var: str):
        self.var = var
    def to_string(self): return f"Next({self.var})"

class Goto(Node):
    def __init__(self, target: str):
        self.target = target
    def to_string(self): return f"Goto({self.target})"

class Gosub(Node):
    def __init__(self, target: str):
        self.target = target
    def to_string(self): return f"Gosub({self.target})"

class Return(Node):
    def to_string(self): return "Return"

class While(Node):
    def __init__(self, condition: Node, body: List[Node]):
        self.condition, self.body = condition, body
    def to_string(self): return "While"
    def children(self):  return [self.condition] + self.body

class Read(Node):
    def __init__(self, vars: List[Node]):
        self.vars = vars
    def to_string(self): return "Read"
    def children(self):  return self.vars

class Input(Node):
    def __init__(self, prompt: str, vars: List[Node]):
        self.prompt, self.vars = prompt, vars
    def to_string(self): return "Input"
    def children(self):  return self.vars

class Dim(Node):
    def __init__(self, vars: List[Node]):
        self.vars = vars
    def to_string(self): return "Dim"
    def children(self):  return self.vars

class Data(Node):
    def __init__(self, values: List[Node]):
        self.values = values
    def to_string(self): return "Data"
    def children(self):  return self.values

class End(Node):
    def to_string(self): return "End"

class BinOp(Node):
    def __init__(self, op: str, left: Node, right: Node):
        self.op, self.left, self.right = op, left, right
    def to_string(self): return f"BinOp({self.op})"
    def children(self):  return [self.left, self.right]

class Number(Node):
    def __init__(self, v: str):
        self.value = float(v) if '.' in v else int(v)
    def to_string(self): return f"Number({self.value})"

class String(Node):
    def __init__(self, v: str):
        self.value = v[1:-1]
    def to_string(self): return f"String(\"{self.value}\")"

class Var(Node):
    def __init__(self, n: str):
        self.name = n
    def to_string(self): return f"Var({self.name})"

class ArrayRef(Node):
    def __init__(self, array: Var, index: Node):
        self.array, self.index = array, index
    def to_string(self): return f"ArrayRef({self.array.name})"
    def children(self):  return [self.array, self.index]

class FuncCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def children(self):
        return self.args

    def to_string(self):
        return f"FuncCall({self.name})"
