from antlr4 import FileStream, CommonTokenStream
from generated.BasicLexer  import BasicLexer
from generated.BasicParser import BasicParser

def parse(path: str):
    stream = FileStream(path, encoding='utf-8')
    lexer  = BasicLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = BasicParser(tokens)
    return parser.program()
