import sys
from basic_compiler.parser    import parse
from basic_compiler.ast.builder import ASTBuilder
from basic_compiler.semantic  import SemanticAnalyzer
from basic_compiler.printer   import print_tree
from basic_compiler.codegen import CodeGenerator
from basic_compiler.optimizer import Optimizer

def compile_and_print(path: str):
    tree = parse(path)
    ast  = ASTBuilder().visit(tree)
    print("=== AST ===")
    print_tree(ast)

    print("\n=== Semantic Check ===")
    SemanticAnalyzer().check(ast)

    print("\n=== Optimized AST ===")
    ast = Optimizer().optimize(ast)
    print_tree(ast)

    print("\n=== Generated Code ===")
    generator = CodeGenerator()
    generator.generate(ast)
    print(generator.get_code())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m basic_compiler.main <file.bas>")
        sys.exit(1)
    compile_and_print(sys.argv[1])
