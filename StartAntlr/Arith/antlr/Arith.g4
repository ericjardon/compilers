grammar Arith;
import CommonLexer;
/** The start rule; begin parsing here. */
prog:   stat+ ; /* entry rule */

stat:   expr NEWLINE     # printExpr           
    |   ID '=' expr NEWLINE        #assign
    |   NEWLINE                    #blank
    ;

expr:   expr ('*'|'/') expr   # MulDiv
    |   expr ('+'|'-') expr   # AddSub
    |   INT                   # INT
    |   ID                    # id
    |   '(' expr ')'         # parens
    ;

MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';