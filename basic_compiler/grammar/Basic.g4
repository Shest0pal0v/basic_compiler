grammar Basic;

program
    : line* EOF
    ;

line
    : (labelDef | (NUMBER? statement?)) NEWLINE
    ;

labelDef
    : (ID | NUMBER) COLON
    ;

statement
    : printStmt
    | letStmt
    | ifStmt
    | gotoStmt
    | forStmt
    | nextStmt
    | gosubStmt
    | returnStmt
    | whileStmt
    | readStmt
    | inputStmt
    | dimStmt
    | dataStmt
    | endStmt
    ;

printStmt    : PRINT exprList? ;
letStmt      : LET variable EQ expression ;
gotoStmt     : GOTO (ID | NUMBER) ;
forStmt      : FOR variable EQ expression TO expression (STEP expression)? ;
nextStmt     : NEXT varRefList ;
gosubStmt    : GOSUB (ID | NUMBER) ;
returnStmt   : RETURN ;
readStmt     : READ varRefList ;
inputStmt    : INPUT (STRING COMMA)? varRefList ;
dimStmt      : DIM varRefList ;
dataStmt     : DATA exprList ;
endStmt      : END ;

// IF
ifStmt
  : IF expression (compOp expression)? THEN statement (ELSE statement)?      # SingleIf
  | IF expression (compOp expression)? THEN NEWLINE
        line*
    (ELSE NEWLINE line*)?
    END IF NEWLINE                                                           # BlockIf
  ;



// WHILE
whileStmt
    : WHILE expression NEWLINE line* WEND
    ;



varRefList
    : varRef (COMMA varRef)*
    ;
varRef
    : arrayRef
    | variable
    ;


exprList
    : expression ( (COMMA | SEMICOLON) expression )*
    ;


expression
    : logicalExpr
    ;

logicalExpr
    : relationalExpr ((AND|OR) relationalExpr)*
    ;

relationalExpr
    : additiveExpr (compOp additiveExpr)?
    ;

additiveExpr
    : multiplicativeExpr ((PLUS|MINUS) multiplicativeExpr)*
    ;

multiplicativeExpr
    : unaryExpr ((MUL|DIV) unaryExpr)*
    ;

unaryExpr
    : (PLUS|MINUS)? atom
    ;

atom
    : NUMBER
    | STRING
    | arrayRef
    | variable
    | LPAREN expression RPAREN
    | funcCall
    ;

arrayRef
    : variable LPAREN expression RPAREN
    ;

funcCall
    : FUNC LPAREN expression (COMMA expression)* RPAREN
    ;

compOp
    : EQ | NEQ | LT | LTE | GT | GTE
    ;


variable
    : ID TYPE_SUFFIX?
    ;


WS                 : [ \t]+               -> skip ;
NEWLINE            : '\r'? '\n'           ;
REM_COMMENT        : 'REM' ~[\r\n]*       -> skip ;
APOSTROPHE_COMMENT : '\'' ~[\r\n]*        -> skip ;

PRINT   : 'PRINT' ;
LET     : 'LET'   ;
IF      : 'IF'    ;
THEN    : 'THEN'  ;
ELSE    : 'ELSE'  ;
END     : 'END'   ;
GOTO    : 'GOTO'  ;
FOR     : 'FOR'   ;
TO      : 'TO'    ;
STEP    : 'STEP'  ;
NEXT    : 'NEXT'  ;
GOSUB   : 'GOSUB' ;
RETURN  : 'RETURN';
WHILE   : 'WHILE' ;
WEND    : 'WEND'  ;
READ    : 'READ'  ;
INPUT   : 'INPUT' ;
DIM     : 'DIM'   ;
DATA    : 'DATA'  ;

AND     : 'AND'   ;
OR      : 'OR'    ;

EQ      : '='     ;
NEQ     : '<>'    ;
LT      : '<'     ;
LTE     : '<='    ;
GT      : '>'     ;
GTE     : '>='    ;
PLUS    : '+'     ;
MINUS   : '-'     ;
MUL     : '*'     ;
DIV     : '/'     ;

LPAREN  : '('     ;
RPAREN  : ')'     ;
COMMA   : ','     ;
SEMICOLON: ';'    ;
COLON   : ':'     ;

ID      : [A-Za-z_] [A-Za-z0-9_]* ;
NUMBER  : [0-9]+ ('.' [0-9]+)? ;
STRING  : '"' (~["\r\n])* '"'   ;

TYPE_SUFFIX
    : '$' | '%' | '!'
    ;

FUNC
    : 'ABS' | 'ASC' | 'ATN' | 'CHR$' | 'COS'
    | 'EXP' | 'INT' | 'LEN' | 'LOG'  | 'MID$'
    | 'PEEK'| 'RND' | 'SIN' | 'SQR'  | 'STR$'
    | 'TAN'
    ;
