from basic_compiler.ast.nodes import Node

def print_tree(node: Node, prefix: str = ""):
    print(prefix + node.to_string())
    for child in node.children():
        print_tree(child, prefix + "    ")
