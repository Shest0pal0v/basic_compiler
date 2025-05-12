# Generated from grammar/Basic.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/")
        buf.write("\u012b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\7\2D\n\2\f\2\16\2G\13\2\3\2")
        buf.write("\3\2\3\3\3\3\5\3M\n\3\3\3\5\3P\n\3\5\3R\n\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5g\n\5\3\6\3\6\5\6k\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t}")
        buf.write("\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\5\16\u008d\n\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u009e\n\22\3\22\3\22\3\22\3\22\5\22\u00a4\n\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u00ab\n\22\3\22\3\22\3\22\7\22")
        buf.write("\u00b0\n\22\f\22\16\22\u00b3\13\22\3\22\3\22\3\22\7\22")
        buf.write("\u00b8\n\22\f\22\16\22\u00bb\13\22\5\22\u00bd\n\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00c3\n\22\3\23\3\23\3\23\3\23\7")
        buf.write("\23\u00c9\n\23\f\23\16\23\u00cc\13\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\7\24\u00d3\n\24\f\24\16\24\u00d6\13\24\3\25\3")
        buf.write("\25\5\25\u00da\n\25\3\26\3\26\3\26\7\26\u00df\n\26\f\26")
        buf.write("\16\26\u00e2\13\26\3\27\3\27\3\30\3\30\3\30\7\30\u00e9")
        buf.write("\n\30\f\30\16\30\u00ec\13\30\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u00f2\n\31\3\32\3\32\3\32\7\32\u00f7\n\32\f\32\16\32")
        buf.write("\u00fa\13\32\3\33\3\33\3\33\7\33\u00ff\n\33\f\33\16\33")
        buf.write("\u0102\13\33\3\34\5\34\u0105\n\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0112\n\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u011e\n\37\f\37\16\37\u0121\13\37\3\37\3\37\3 \3 \3!")
        buf.write("\3!\5!\u0129\n!\3!\2\2\"\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@\2\b\3\2+,\3\2()\3")
        buf.write("\2\32\33\3\2\"#\3\2$%\3\2\34!\2\u0135\2E\3\2\2\2\4Q\3")
        buf.write("\2\2\2\6U\3\2\2\2\bf\3\2\2\2\nh\3\2\2\2\fl\3\2\2\2\16")
        buf.write("q\3\2\2\2\20t\3\2\2\2\22~\3\2\2\2\24\u0081\3\2\2\2\26")
        buf.write("\u0084\3\2\2\2\30\u0086\3\2\2\2\32\u0089\3\2\2\2\34\u0090")
        buf.write("\3\2\2\2\36\u0093\3\2\2\2 \u0096\3\2\2\2\"\u00c2\3\2\2")
        buf.write("\2$\u00c4\3\2\2\2&\u00cf\3\2\2\2(\u00d9\3\2\2\2*\u00db")
        buf.write("\3\2\2\2,\u00e3\3\2\2\2.\u00e5\3\2\2\2\60\u00ed\3\2\2")
        buf.write("\2\62\u00f3\3\2\2\2\64\u00fb\3\2\2\2\66\u0104\3\2\2\2")
        buf.write("8\u0111\3\2\2\2:\u0113\3\2\2\2<\u0118\3\2\2\2>\u0124\3")
        buf.write("\2\2\2@\u0126\3\2\2\2BD\5\4\3\2CB\3\2\2\2DG\3\2\2\2EC")
        buf.write("\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\7\2\2\3I\3\3")
        buf.write("\2\2\2JR\5\6\4\2KM\7,\2\2LK\3\2\2\2LM\3\2\2\2MO\3\2\2")
        buf.write("\2NP\5\b\5\2ON\3\2\2\2OP\3\2\2\2PR\3\2\2\2QJ\3\2\2\2Q")
        buf.write("L\3\2\2\2RS\3\2\2\2ST\7\4\2\2T\5\3\2\2\2UV\t\2\2\2VW\7")
        buf.write("*\2\2W\7\3\2\2\2Xg\5\n\6\2Yg\5\f\7\2Zg\5\"\22\2[g\5\16")
        buf.write("\b\2\\g\5\20\t\2]g\5\22\n\2^g\5\24\13\2_g\5\26\f\2`g\5")
        buf.write("$\23\2ag\5\30\r\2bg\5\32\16\2cg\5\34\17\2dg\5\36\20\2")
        buf.write("eg\5 \21\2fX\3\2\2\2fY\3\2\2\2fZ\3\2\2\2f[\3\2\2\2f\\")
        buf.write("\3\2\2\2f]\3\2\2\2f^\3\2\2\2f_\3\2\2\2f`\3\2\2\2fa\3\2")
        buf.write("\2\2fb\3\2\2\2fc\3\2\2\2fd\3\2\2\2fe\3\2\2\2g\t\3\2\2")
        buf.write("\2hj\7\7\2\2ik\5*\26\2ji\3\2\2\2jk\3\2\2\2k\13\3\2\2\2")
        buf.write("lm\7\b\2\2mn\5@!\2no\7\34\2\2op\5,\27\2p\r\3\2\2\2qr\7")
        buf.write("\r\2\2rs\t\2\2\2s\17\3\2\2\2tu\7\16\2\2uv\5@!\2vw\7\34")
        buf.write("\2\2wx\5,\27\2xy\7\17\2\2y|\5,\27\2z{\7\20\2\2{}\5,\27")
        buf.write("\2|z\3\2\2\2|}\3\2\2\2}\21\3\2\2\2~\177\7\21\2\2\177\u0080")
        buf.write("\5&\24\2\u0080\23\3\2\2\2\u0081\u0082\7\22\2\2\u0082\u0083")
        buf.write("\t\2\2\2\u0083\25\3\2\2\2\u0084\u0085\7\23\2\2\u0085\27")
        buf.write("\3\2\2\2\u0086\u0087\7\26\2\2\u0087\u0088\5&\24\2\u0088")
        buf.write("\31\3\2\2\2\u0089\u008c\7\27\2\2\u008a\u008b\7-\2\2\u008b")
        buf.write("\u008d\7(\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u008f\5&\24\2\u008f\33\3\2")
        buf.write("\2\2\u0090\u0091\7\30\2\2\u0091\u0092\5&\24\2\u0092\35")
        buf.write("\3\2\2\2\u0093\u0094\7\31\2\2\u0094\u0095\5*\26\2\u0095")
        buf.write("\37\3\2\2\2\u0096\u0097\7\f\2\2\u0097!\3\2\2\2\u0098\u0099")
        buf.write("\7\t\2\2\u0099\u009d\5,\27\2\u009a\u009b\5> \2\u009b\u009c")
        buf.write("\5,\27\2\u009c\u009e\3\2\2\2\u009d\u009a\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\7\n\2\2")
        buf.write("\u00a0\u00a3\5\b\5\2\u00a1\u00a2\7\13\2\2\u00a2\u00a4")
        buf.write("\5\b\5\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00c3\3\2\2\2\u00a5\u00a6\7\t\2\2\u00a6\u00aa\5,\27\2")
        buf.write("\u00a7\u00a8\5> \2\u00a8\u00a9\5,\27\2\u00a9\u00ab\3\2")
        buf.write("\2\2\u00aa\u00a7\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac")
        buf.write("\3\2\2\2\u00ac\u00ad\7\n\2\2\u00ad\u00b1\7\4\2\2\u00ae")
        buf.write("\u00b0\5\4\3\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00bc\3")
        buf.write("\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7\13\2\2\u00b5")
        buf.write("\u00b9\7\4\2\2\u00b6\u00b8\5\4\3\2\u00b7\u00b6\3\2\2\2")
        buf.write("\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3")
        buf.write("\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00b4")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\7\f\2\2\u00bf\u00c0\7\t\2\2\u00c0\u00c1\7\4\2\2")
        buf.write("\u00c1\u00c3\3\2\2\2\u00c2\u0098\3\2\2\2\u00c2\u00a5\3")
        buf.write("\2\2\2\u00c3#\3\2\2\2\u00c4\u00c5\7\24\2\2\u00c5\u00c6")
        buf.write("\5,\27\2\u00c6\u00ca\7\4\2\2\u00c7\u00c9\5\4\3\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ca\3")
        buf.write("\2\2\2\u00cd\u00ce\7\25\2\2\u00ce%\3\2\2\2\u00cf\u00d4")
        buf.write("\5(\25\2\u00d0\u00d1\7(\2\2\u00d1\u00d3\5(\25\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\'\3\2\2\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d7\u00da\5:\36\2\u00d8\u00da\5@!\2\u00d9\u00d7\3")
        buf.write("\2\2\2\u00d9\u00d8\3\2\2\2\u00da)\3\2\2\2\u00db\u00e0")
        buf.write("\5,\27\2\u00dc\u00dd\t\3\2\2\u00dd\u00df\5,\27\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1+\3\2\2\2\u00e2\u00e0\3\2\2")
        buf.write("\2\u00e3\u00e4\5.\30\2\u00e4-\3\2\2\2\u00e5\u00ea\5\60")
        buf.write("\31\2\u00e6\u00e7\t\4\2\2\u00e7\u00e9\5\60\31\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb/\3\2\2\2\u00ec\u00ea\3\2\2")
        buf.write("\2\u00ed\u00f1\5\62\32\2\u00ee\u00ef\5> \2\u00ef\u00f0")
        buf.write("\5\62\32\2\u00f0\u00f2\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f1")
        buf.write("\u00f2\3\2\2\2\u00f2\61\3\2\2\2\u00f3\u00f8\5\64\33\2")
        buf.write("\u00f4\u00f5\t\5\2\2\u00f5\u00f7\5\64\33\2\u00f6\u00f4")
        buf.write("\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\63\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb")
        buf.write("\u0100\5\66\34\2\u00fc\u00fd\t\6\2\2\u00fd\u00ff\5\66")
        buf.write("\34\2\u00fe\u00fc\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\65\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0103\u0105\t\5\2\2\u0104\u0103\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\58\35\2")
        buf.write("\u0107\67\3\2\2\2\u0108\u0112\7,\2\2\u0109\u0112\7-\2")
        buf.write("\2\u010a\u0112\5:\36\2\u010b\u0112\5@!\2\u010c\u010d\7")
        buf.write("&\2\2\u010d\u010e\5,\27\2\u010e\u010f\7\'\2\2\u010f\u0112")
        buf.write("\3\2\2\2\u0110\u0112\5<\37\2\u0111\u0108\3\2\2\2\u0111")
        buf.write("\u0109\3\2\2\2\u0111\u010a\3\2\2\2\u0111\u010b\3\2\2\2")
        buf.write("\u0111\u010c\3\2\2\2\u0111\u0110\3\2\2\2\u01129\3\2\2")
        buf.write("\2\u0113\u0114\5@!\2\u0114\u0115\7&\2\2\u0115\u0116\5")
        buf.write(",\27\2\u0116\u0117\7\'\2\2\u0117;\3\2\2\2\u0118\u0119")
        buf.write("\7/\2\2\u0119\u011a\7&\2\2\u011a\u011f\5,\27\2\u011b\u011c")
        buf.write("\7(\2\2\u011c\u011e\5,\27\2\u011d\u011b\3\2\2\2\u011e")
        buf.write("\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u0122\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0123\7")
        buf.write("\'\2\2\u0123=\3\2\2\2\u0124\u0125\t\7\2\2\u0125?\3\2\2")
        buf.write("\2\u0126\u0128\7+\2\2\u0127\u0129\7.\2\2\u0128\u0127\3")
        buf.write("\2\2\2\u0128\u0129\3\2\2\2\u0129A\3\2\2\2\35ELOQfj|\u008c")
        buf.write("\u009d\u00a3\u00aa\u00b1\u00b9\u00bc\u00c2\u00ca\u00d4")
        buf.write("\u00d9\u00e0\u00ea\u00f1\u00f8\u0100\u0104\u0111\u011f")
        buf.write("\u0128")
        return buf.getvalue()


class BasicParser ( Parser ):

    grammarFileName = "Basic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'PRINT'", "'LET'", "'IF'", "'THEN'", 
                     "'ELSE'", "'END'", "'GOTO'", "'FOR'", "'TO'", "'STEP'", 
                     "'NEXT'", "'GOSUB'", "'RETURN'", "'WHILE'", "'WEND'", 
                     "'READ'", "'INPUT'", "'DIM'", "'DATA'", "'AND'", "'OR'", 
                     "'='", "'<>'", "'<'", "'<='", "'>'", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'('", "')'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "WS", "NEWLINE", "REM_COMMENT", "APOSTROPHE_COMMENT", 
                      "PRINT", "LET", "IF", "THEN", "ELSE", "END", "GOTO", 
                      "FOR", "TO", "STEP", "NEXT", "GOSUB", "RETURN", "WHILE", 
                      "WEND", "READ", "INPUT", "DIM", "DATA", "AND", "OR", 
                      "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "PLUS", "MINUS", 
                      "MUL", "DIV", "LPAREN", "RPAREN", "COMMA", "SEMICOLON", 
                      "COLON", "ID", "NUMBER", "STRING", "TYPE_SUFFIX", 
                      "FUNC" ]

    RULE_program = 0
    RULE_line = 1
    RULE_labelDef = 2
    RULE_statement = 3
    RULE_printStmt = 4
    RULE_letStmt = 5
    RULE_gotoStmt = 6
    RULE_forStmt = 7
    RULE_nextStmt = 8
    RULE_gosubStmt = 9
    RULE_returnStmt = 10
    RULE_readStmt = 11
    RULE_inputStmt = 12
    RULE_dimStmt = 13
    RULE_dataStmt = 14
    RULE_endStmt = 15
    RULE_ifStmt = 16
    RULE_whileStmt = 17
    RULE_varRefList = 18
    RULE_varRef = 19
    RULE_exprList = 20
    RULE_expression = 21
    RULE_logicalExpr = 22
    RULE_relationalExpr = 23
    RULE_additiveExpr = 24
    RULE_multiplicativeExpr = 25
    RULE_unaryExpr = 26
    RULE_atom = 27
    RULE_arrayRef = 28
    RULE_funcCall = 29
    RULE_compOp = 30
    RULE_variable = 31

    ruleNames =  [ "program", "line", "labelDef", "statement", "printStmt", 
                   "letStmt", "gotoStmt", "forStmt", "nextStmt", "gosubStmt", 
                   "returnStmt", "readStmt", "inputStmt", "dimStmt", "dataStmt", 
                   "endStmt", "ifStmt", "whileStmt", "varRefList", "varRef", 
                   "exprList", "expression", "logicalExpr", "relationalExpr", 
                   "additiveExpr", "multiplicativeExpr", "unaryExpr", "atom", 
                   "arrayRef", "funcCall", "compOp", "variable" ]

    EOF = Token.EOF
    WS=1
    NEWLINE=2
    REM_COMMENT=3
    APOSTROPHE_COMMENT=4
    PRINT=5
    LET=6
    IF=7
    THEN=8
    ELSE=9
    END=10
    GOTO=11
    FOR=12
    TO=13
    STEP=14
    NEXT=15
    GOSUB=16
    RETURN=17
    WHILE=18
    WEND=19
    READ=20
    INPUT=21
    DIM=22
    DATA=23
    AND=24
    OR=25
    EQ=26
    NEQ=27
    LT=28
    LTE=29
    GT=30
    GTE=31
    PLUS=32
    MINUS=33
    MUL=34
    DIV=35
    LPAREN=36
    RPAREN=37
    COMMA=38
    SEMICOLON=39
    COLON=40
    ID=41
    NUMBER=42
    STRING=43
    TYPE_SUFFIX=44
    FUNC=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BasicParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.LineContext)
            else:
                return self.getTypedRuleContext(BasicParser.LineContext,i)


        def getRuleIndex(self):
            return BasicParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BasicParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicParser.NEWLINE) | (1 << BasicParser.PRINT) | (1 << BasicParser.LET) | (1 << BasicParser.IF) | (1 << BasicParser.END) | (1 << BasicParser.GOTO) | (1 << BasicParser.FOR) | (1 << BasicParser.NEXT) | (1 << BasicParser.GOSUB) | (1 << BasicParser.RETURN) | (1 << BasicParser.WHILE) | (1 << BasicParser.READ) | (1 << BasicParser.INPUT) | (1 << BasicParser.DIM) | (1 << BasicParser.DATA) | (1 << BasicParser.ID) | (1 << BasicParser.NUMBER))) != 0):
                self.state = 64
                self.line()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(BasicParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(BasicParser.NEWLINE, 0)

        def labelDef(self):
            return self.getTypedRuleContext(BasicParser.LabelDefContext,0)


        def NUMBER(self):
            return self.getToken(BasicParser.NUMBER, 0)

        def statement(self):
            return self.getTypedRuleContext(BasicParser.StatementContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = BasicParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 72
                self.labelDef()
                pass

            elif la_ == 2:
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BasicParser.NUMBER:
                    self.state = 73
                    self.match(BasicParser.NUMBER)


                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicParser.PRINT) | (1 << BasicParser.LET) | (1 << BasicParser.IF) | (1 << BasicParser.END) | (1 << BasicParser.GOTO) | (1 << BasicParser.FOR) | (1 << BasicParser.NEXT) | (1 << BasicParser.GOSUB) | (1 << BasicParser.RETURN) | (1 << BasicParser.WHILE) | (1 << BasicParser.READ) | (1 << BasicParser.INPUT) | (1 << BasicParser.DIM) | (1 << BasicParser.DATA))) != 0):
                    self.state = 76
                    self.statement()


                pass


            self.state = 81
            self.match(BasicParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(BasicParser.COLON, 0)

        def ID(self):
            return self.getToken(BasicParser.ID, 0)

        def NUMBER(self):
            return self.getToken(BasicParser.NUMBER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_labelDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelDef" ):
                listener.enterLabelDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelDef" ):
                listener.exitLabelDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelDef" ):
                return visitor.visitLabelDef(self)
            else:
                return visitor.visitChildren(self)




    def labelDef(self):

        localctx = BasicParser.LabelDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_labelDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not(_la==BasicParser.ID or _la==BasicParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 84
            self.match(BasicParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printStmt(self):
            return self.getTypedRuleContext(BasicParser.PrintStmtContext,0)


        def letStmt(self):
            return self.getTypedRuleContext(BasicParser.LetStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BasicParser.IfStmtContext,0)


        def gotoStmt(self):
            return self.getTypedRuleContext(BasicParser.GotoStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BasicParser.ForStmtContext,0)


        def nextStmt(self):
            return self.getTypedRuleContext(BasicParser.NextStmtContext,0)


        def gosubStmt(self):
            return self.getTypedRuleContext(BasicParser.GosubStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BasicParser.ReturnStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(BasicParser.WhileStmtContext,0)


        def readStmt(self):
            return self.getTypedRuleContext(BasicParser.ReadStmtContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(BasicParser.InputStmtContext,0)


        def dimStmt(self):
            return self.getTypedRuleContext(BasicParser.DimStmtContext,0)


        def dataStmt(self):
            return self.getTypedRuleContext(BasicParser.DataStmtContext,0)


        def endStmt(self):
            return self.getTypedRuleContext(BasicParser.EndStmtContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BasicParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasicParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.printStmt()
                pass
            elif token in [BasicParser.LET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.letStmt()
                pass
            elif token in [BasicParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.ifStmt()
                pass
            elif token in [BasicParser.GOTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.gotoStmt()
                pass
            elif token in [BasicParser.FOR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.forStmt()
                pass
            elif token in [BasicParser.NEXT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.nextStmt()
                pass
            elif token in [BasicParser.GOSUB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 92
                self.gosubStmt()
                pass
            elif token in [BasicParser.RETURN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 93
                self.returnStmt()
                pass
            elif token in [BasicParser.WHILE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 94
                self.whileStmt()
                pass
            elif token in [BasicParser.READ]:
                self.enterOuterAlt(localctx, 10)
                self.state = 95
                self.readStmt()
                pass
            elif token in [BasicParser.INPUT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 96
                self.inputStmt()
                pass
            elif token in [BasicParser.DIM]:
                self.enterOuterAlt(localctx, 12)
                self.state = 97
                self.dimStmt()
                pass
            elif token in [BasicParser.DATA]:
                self.enterOuterAlt(localctx, 13)
                self.state = 98
                self.dataStmt()
                pass
            elif token in [BasicParser.END]:
                self.enterOuterAlt(localctx, 14)
                self.state = 99
                self.endStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BasicParser.PRINT, 0)

        def exprList(self):
            return self.getTypedRuleContext(BasicParser.ExprListContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = BasicParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BasicParser.PRINT)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicParser.PLUS) | (1 << BasicParser.MINUS) | (1 << BasicParser.LPAREN) | (1 << BasicParser.ID) | (1 << BasicParser.NUMBER) | (1 << BasicParser.STRING) | (1 << BasicParser.FUNC))) != 0):
                self.state = 103
                self.exprList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(BasicParser.LET, 0)

        def variable(self):
            return self.getTypedRuleContext(BasicParser.VariableContext,0)


        def EQ(self):
            return self.getToken(BasicParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_letStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStmt" ):
                listener.enterLetStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStmt" ):
                listener.exitLetStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStmt" ):
                return visitor.visitLetStmt(self)
            else:
                return visitor.visitChildren(self)




    def letStmt(self):

        localctx = BasicParser.LetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_letStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(BasicParser.LET)
            self.state = 107
            self.variable()
            self.state = 108
            self.match(BasicParser.EQ)
            self.state = 109
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(BasicParser.GOTO, 0)

        def ID(self):
            return self.getToken(BasicParser.ID, 0)

        def NUMBER(self):
            return self.getToken(BasicParser.NUMBER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_gotoStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoStmt" ):
                listener.enterGotoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoStmt" ):
                listener.exitGotoStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoStmt" ):
                return visitor.visitGotoStmt(self)
            else:
                return visitor.visitChildren(self)




    def gotoStmt(self):

        localctx = BasicParser.GotoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_gotoStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(BasicParser.GOTO)
            self.state = 112
            _la = self._input.LA(1)
            if not(_la==BasicParser.ID or _la==BasicParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BasicParser.FOR, 0)

        def variable(self):
            return self.getTypedRuleContext(BasicParser.VariableContext,0)


        def EQ(self):
            return self.getToken(BasicParser.EQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(BasicParser.TO, 0)

        def STEP(self):
            return self.getToken(BasicParser.STEP, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BasicParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(BasicParser.FOR)
            self.state = 115
            self.variable()
            self.state = 116
            self.match(BasicParser.EQ)
            self.state = 117
            self.expression()
            self.state = 118
            self.match(BasicParser.TO)
            self.state = 119
            self.expression()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicParser.STEP:
                self.state = 120
                self.match(BasicParser.STEP)
                self.state = 121
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NextStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEXT(self):
            return self.getToken(BasicParser.NEXT, 0)

        def varRefList(self):
            return self.getTypedRuleContext(BasicParser.VarRefListContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_nextStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNextStmt" ):
                listener.enterNextStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNextStmt" ):
                listener.exitNextStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextStmt" ):
                return visitor.visitNextStmt(self)
            else:
                return visitor.visitChildren(self)




    def nextStmt(self):

        localctx = BasicParser.NextStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_nextStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(BasicParser.NEXT)
            self.state = 125
            self.varRefList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GosubStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOSUB(self):
            return self.getToken(BasicParser.GOSUB, 0)

        def ID(self):
            return self.getToken(BasicParser.ID, 0)

        def NUMBER(self):
            return self.getToken(BasicParser.NUMBER, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_gosubStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGosubStmt" ):
                listener.enterGosubStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGosubStmt" ):
                listener.exitGosubStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGosubStmt" ):
                return visitor.visitGosubStmt(self)
            else:
                return visitor.visitChildren(self)




    def gosubStmt(self):

        localctx = BasicParser.GosubStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_gosubStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(BasicParser.GOSUB)
            self.state = 128
            _la = self._input.LA(1)
            if not(_la==BasicParser.ID or _la==BasicParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BasicParser.RETURN, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BasicParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(BasicParser.RETURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(BasicParser.READ, 0)

        def varRefList(self):
            return self.getTypedRuleContext(BasicParser.VarRefListContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_readStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)




    def readStmt(self):

        localctx = BasicParser.ReadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_readStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BasicParser.READ)
            self.state = 133
            self.varRefList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(BasicParser.INPUT, 0)

        def varRefList(self):
            return self.getTypedRuleContext(BasicParser.VarRefListContext,0)


        def STRING(self):
            return self.getToken(BasicParser.STRING, 0)

        def COMMA(self):
            return self.getToken(BasicParser.COMMA, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_inputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStmt" ):
                return visitor.visitInputStmt(self)
            else:
                return visitor.visitChildren(self)




    def inputStmt(self):

        localctx = BasicParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inputStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(BasicParser.INPUT)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicParser.STRING:
                self.state = 136
                self.match(BasicParser.STRING)
                self.state = 137
                self.match(BasicParser.COMMA)


            self.state = 140
            self.varRefList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIM(self):
            return self.getToken(BasicParser.DIM, 0)

        def varRefList(self):
            return self.getTypedRuleContext(BasicParser.VarRefListContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_dimStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimStmt" ):
                listener.enterDimStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimStmt" ):
                listener.exitDimStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimStmt" ):
                return visitor.visitDimStmt(self)
            else:
                return visitor.visitChildren(self)




    def dimStmt(self):

        localctx = BasicParser.DimStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dimStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(BasicParser.DIM)
            self.state = 143
            self.varRefList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(BasicParser.DATA, 0)

        def exprList(self):
            return self.getTypedRuleContext(BasicParser.ExprListContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_dataStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataStmt" ):
                listener.enterDataStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataStmt" ):
                listener.exitDataStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataStmt" ):
                return visitor.visitDataStmt(self)
            else:
                return visitor.visitChildren(self)




    def dataStmt(self):

        localctx = BasicParser.DataStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dataStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BasicParser.DATA)
            self.state = 146
            self.exprList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(BasicParser.END, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_endStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndStmt" ):
                listener.enterEndStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndStmt" ):
                listener.exitEndStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndStmt" ):
                return visitor.visitEndStmt(self)
            else:
                return visitor.visitChildren(self)




    def endStmt(self):

        localctx = BasicParser.EndStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_endStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(BasicParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicParser.RULE_ifStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlockIfContext(IfStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicParser.IfStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.IF)
            else:
                return self.getToken(BasicParser.IF, i)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)

        def THEN(self):
            return self.getToken(BasicParser.THEN, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.NEWLINE)
            else:
                return self.getToken(BasicParser.NEWLINE, i)
        def END(self):
            return self.getToken(BasicParser.END, 0)
        def compOp(self):
            return self.getTypedRuleContext(BasicParser.CompOpContext,0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.LineContext)
            else:
                return self.getTypedRuleContext(BasicParser.LineContext,i)

        def ELSE(self):
            return self.getToken(BasicParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockIf" ):
                listener.enterBlockIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockIf" ):
                listener.exitBlockIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockIf" ):
                return visitor.visitBlockIf(self)
            else:
                return visitor.visitChildren(self)


    class SingleIfContext(IfStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicParser.IfStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(BasicParser.IF, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)

        def THEN(self):
            return self.getToken(BasicParser.THEN, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasicParser.StatementContext,i)

        def compOp(self):
            return self.getTypedRuleContext(BasicParser.CompOpContext,0)

        def ELSE(self):
            return self.getToken(BasicParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleIf" ):
                listener.enterSingleIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleIf" ):
                listener.exitSingleIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleIf" ):
                return visitor.visitSingleIf(self)
            else:
                return visitor.visitChildren(self)



    def ifStmt(self):

        localctx = BasicParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = BasicParser.SingleIfContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(BasicParser.IF)
                self.state = 151
                self.expression()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicParser.EQ) | (1 << BasicParser.NEQ) | (1 << BasicParser.LT) | (1 << BasicParser.LTE) | (1 << BasicParser.GT) | (1 << BasicParser.GTE))) != 0):
                    self.state = 152
                    self.compOp()
                    self.state = 153
                    self.expression()


                self.state = 157
                self.match(BasicParser.THEN)
                self.state = 158
                self.statement()
                self.state = 161
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 159
                    self.match(BasicParser.ELSE)
                    self.state = 160
                    self.statement()


                pass

            elif la_ == 2:
                localctx = BasicParser.BlockIfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(BasicParser.IF)
                self.state = 164
                self.expression()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicParser.EQ) | (1 << BasicParser.NEQ) | (1 << BasicParser.LT) | (1 << BasicParser.LTE) | (1 << BasicParser.GT) | (1 << BasicParser.GTE))) != 0):
                    self.state = 165
                    self.compOp()
                    self.state = 166
                    self.expression()


                self.state = 170
                self.match(BasicParser.THEN)
                self.state = 171
                self.match(BasicParser.NEWLINE)
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 172
                        self.line() 
                    self.state = 177
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BasicParser.ELSE:
                    self.state = 178
                    self.match(BasicParser.ELSE)
                    self.state = 179
                    self.match(BasicParser.NEWLINE)
                    self.state = 183
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 180
                            self.line() 
                        self.state = 185
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)



                self.state = 188
                self.match(BasicParser.END)
                self.state = 189
                self.match(BasicParser.IF)
                self.state = 190
                self.match(BasicParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BasicParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(BasicParser.NEWLINE, 0)

        def WEND(self):
            return self.getToken(BasicParser.WEND, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.LineContext)
            else:
                return self.getTypedRuleContext(BasicParser.LineContext,i)


        def getRuleIndex(self):
            return BasicParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = BasicParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(BasicParser.WHILE)
            self.state = 195
            self.expression()
            self.state = 196
            self.match(BasicParser.NEWLINE)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicParser.NEWLINE) | (1 << BasicParser.PRINT) | (1 << BasicParser.LET) | (1 << BasicParser.IF) | (1 << BasicParser.END) | (1 << BasicParser.GOTO) | (1 << BasicParser.FOR) | (1 << BasicParser.NEXT) | (1 << BasicParser.GOSUB) | (1 << BasicParser.RETURN) | (1 << BasicParser.WHILE) | (1 << BasicParser.READ) | (1 << BasicParser.INPUT) | (1 << BasicParser.DIM) | (1 << BasicParser.DATA) | (1 << BasicParser.ID) | (1 << BasicParser.NUMBER))) != 0):
                self.state = 197
                self.line()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self.match(BasicParser.WEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarRefListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varRef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.VarRefContext)
            else:
                return self.getTypedRuleContext(BasicParser.VarRefContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.COMMA)
            else:
                return self.getToken(BasicParser.COMMA, i)

        def getRuleIndex(self):
            return BasicParser.RULE_varRefList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarRefList" ):
                listener.enterVarRefList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarRefList" ):
                listener.exitVarRefList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarRefList" ):
                return visitor.visitVarRefList(self)
            else:
                return visitor.visitChildren(self)




    def varRefList(self):

        localctx = BasicParser.VarRefListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_varRefList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.varRef()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicParser.COMMA:
                self.state = 206
                self.match(BasicParser.COMMA)
                self.state = 207
                self.varRef()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayRef(self):
            return self.getTypedRuleContext(BasicParser.ArrayRefContext,0)


        def variable(self):
            return self.getTypedRuleContext(BasicParser.VariableContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_varRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarRef" ):
                listener.enterVarRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarRef" ):
                listener.exitVarRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarRef" ):
                return visitor.visitVarRef(self)
            else:
                return visitor.visitChildren(self)




    def varRef(self):

        localctx = BasicParser.VarRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_varRef)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.arrayRef()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.COMMA)
            else:
                return self.getToken(BasicParser.COMMA, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.SEMICOLON)
            else:
                return self.getToken(BasicParser.SEMICOLON, i)

        def getRuleIndex(self):
            return BasicParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = BasicParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.expression()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicParser.COMMA or _la==BasicParser.SEMICOLON:
                self.state = 218
                _la = self._input.LA(1)
                if not(_la==BasicParser.COMMA or _la==BasicParser.SEMICOLON):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 219
                self.expression()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpr(self):
            return self.getTypedRuleContext(BasicParser.LogicalExprContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BasicParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.logicalExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(BasicParser.RelationalExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.AND)
            else:
                return self.getToken(BasicParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.OR)
            else:
                return self.getToken(BasicParser.OR, i)

        def getRuleIndex(self):
            return BasicParser.RULE_logicalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalExpr(self):

        localctx = BasicParser.LogicalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_logicalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.relationalExpr()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicParser.AND or _la==BasicParser.OR:
                self.state = 228
                _la = self._input.LA(1)
                if not(_la==BasicParser.AND or _la==BasicParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self.relationalExpr()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(BasicParser.AdditiveExprContext,i)


        def compOp(self):
            return self.getTypedRuleContext(BasicParser.CompOpContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = BasicParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_relationalExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.additiveExpr()
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 236
                self.compOp()
                self.state = 237
                self.additiveExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(BasicParser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.PLUS)
            else:
                return self.getToken(BasicParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.MINUS)
            else:
                return self.getToken(BasicParser.MINUS, i)

        def getRuleIndex(self):
            return BasicParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = BasicParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.multiplicativeExpr()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicParser.PLUS or _la==BasicParser.MINUS:
                self.state = 242
                _la = self._input.LA(1)
                if not(_la==BasicParser.PLUS or _la==BasicParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 243
                self.multiplicativeExpr()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(BasicParser.UnaryExprContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.MUL)
            else:
                return self.getToken(BasicParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.DIV)
            else:
                return self.getToken(BasicParser.DIV, i)

        def getRuleIndex(self):
            return BasicParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = BasicParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.unaryExpr()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicParser.MUL or _la==BasicParser.DIV:
                self.state = 250
                _la = self._input.LA(1)
                if not(_la==BasicParser.MUL or _la==BasicParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 251
                self.unaryExpr()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(BasicParser.AtomContext,0)


        def PLUS(self):
            return self.getToken(BasicParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BasicParser.MINUS, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = BasicParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicParser.PLUS or _la==BasicParser.MINUS:
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==BasicParser.PLUS or _la==BasicParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 260
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(BasicParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(BasicParser.STRING, 0)

        def arrayRef(self):
            return self.getTypedRuleContext(BasicParser.ArrayRefContext,0)


        def variable(self):
            return self.getTypedRuleContext(BasicParser.VariableContext,0)


        def LPAREN(self):
            return self.getToken(BasicParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicParser.RPAREN, 0)

        def funcCall(self):
            return self.getTypedRuleContext(BasicParser.FuncCallContext,0)


        def getRuleIndex(self):
            return BasicParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = BasicParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_atom)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(BasicParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(BasicParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.arrayRef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.variable()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 266
                self.match(BasicParser.LPAREN)
                self.state = 267
                self.expression()
                self.state = 268
                self.match(BasicParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 270
                self.funcCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BasicParser.VariableContext,0)


        def LPAREN(self):
            return self.getToken(BasicParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_arrayRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayRef" ):
                listener.enterArrayRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayRef" ):
                listener.exitArrayRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayRef" ):
                return visitor.visitArrayRef(self)
            else:
                return visitor.visitChildren(self)




    def arrayRef(self):

        localctx = BasicParser.ArrayRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrayRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.variable()
            self.state = 274
            self.match(BasicParser.LPAREN)
            self.state = 275
            self.expression()
            self.state = 276
            self.match(BasicParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(BasicParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(BasicParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(BasicParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicParser.COMMA)
            else:
                return self.getToken(BasicParser.COMMA, i)

        def getRuleIndex(self):
            return BasicParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = BasicParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(BasicParser.FUNC)
            self.state = 279
            self.match(BasicParser.LPAREN)
            self.state = 280
            self.expression()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicParser.COMMA:
                self.state = 281
                self.match(BasicParser.COMMA)
                self.state = 282
                self.expression()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
            self.match(BasicParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(BasicParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BasicParser.NEQ, 0)

        def LT(self):
            return self.getToken(BasicParser.LT, 0)

        def LTE(self):
            return self.getToken(BasicParser.LTE, 0)

        def GT(self):
            return self.getToken(BasicParser.GT, 0)

        def GTE(self):
            return self.getToken(BasicParser.GTE, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOp" ):
                return visitor.visitCompOp(self)
            else:
                return visitor.visitChildren(self)




    def compOp(self):

        localctx = BasicParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicParser.EQ) | (1 << BasicParser.NEQ) | (1 << BasicParser.LT) | (1 << BasicParser.LTE) | (1 << BasicParser.GT) | (1 << BasicParser.GTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicParser.ID, 0)

        def TYPE_SUFFIX(self):
            return self.getToken(BasicParser.TYPE_SUFFIX, 0)

        def getRuleIndex(self):
            return BasicParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BasicParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BasicParser.ID)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicParser.TYPE_SUFFIX:
                self.state = 293
                self.match(BasicParser.TYPE_SUFFIX)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





