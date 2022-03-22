grammar basic2;

program : statement+;

expression: 
    expression '+' expression       #suma
    | expression '-' expression     #resta
    | '(' expression ')'            #parens
    | Numero                        #primaria
    | Variable                      #var
    ;

statement:
    'int' Variable                  #declaracion
    | Variable '=' expression       #asignacion
    | 'print' '(' expression ')'    #printint
    ;

// Tokens (capitalized)
Numero : [0-9]+;
Variable : [a-z]+;
WS : [ \t\n\r]+ -> skip ;

