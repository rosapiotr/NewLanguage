grammar Lang;
prog:   ((expr|function|functionCall)? NEWLINE)* EOF    
    ;
expr
   :   operation
   |   write
   |   read
   |   assign
   |   ifExpr
   |   whileExpr
   ;

operation
   :   '(' operation ')'                         # parensExpr
   |   left=operation op=('*'|'/') right=operation    # infixExpr
   |   left=operation op=('+'|'-') right=operation    # infixExpr
   |   value                                # numberExpr
   ;

value
   :   number
   |   ID
   |   STRING
   ;

write
   :   WRITE operation ')'
   ;

read
   :   ID ASSIGN READ '(' typ ')'
   ;

typ
   :   INTEGER
   |   DOUBLE
   |   STR
   ;

assign
   :   ID ASSIGN operation
   ;

number
   :   INT
   |   REAL
   ;

ifExpr
   :   IF left=value comp right=value ')' '{' (expr? NEWLINE)* '}'
   ;

whileExpr
   :   WHILE left=ID comp right=value ')' '{' (expr? NEWLINE)* '}'
   ;

function
   :   FUNCTION fname=ID '(' params=functionparam? ')' '{' (expr? NEWLINE)* '}'
   ;

FUNCTION:   'function'
   ;

functionparam
   :   (typ ID ',')* typ ID
   ;

functionCall
   :   fname=ID '(' params=functioncallparam? ')'
   ;

functioncallparam
   :   (value ',')* value
   ;

IF:   'if('
   ;

WHILE:   'while('
   ;

comp
   :   GE
   |   LE
   |   GT
   |   LT
   |   EQ
   ;   

GE:   '>='
   ;

LE:   '<='
   ;

GT:   '>'
   ;

LT:   '<'
   ;

EQ:
   '=='
   ;

INTEGER:   'int'
   ;

DOUBLE:   'double'
   ;

STR:   'str'
   ;

WRITE:   'write('
   ;

READ:   'read'
   ;

ASSIGN:   '='
   ;

ID:   ('a'..'z'|'A'..'Z')+
   ;

STRING:   '"' ( ~('\\'|'"') )* '"'
   ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
INT: ('0'..'9')+;
REAL: [0-9]+'.'[0-9]+;
NUM :   [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?;
NEWLINE:	'\r'? '\n';
WS  :   [ \t\r\n] -> channel(HIDDEN);
