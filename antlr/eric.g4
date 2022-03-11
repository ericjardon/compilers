grammar eric;

let : VAR '=' (INT | STR);
show: 'show' (INT | STR | VAR);

expression: 
    expression '+' expression
    | INT           
    | STR           
    | VAR           
    ;

statement:
    let |
    show
    ;

program : (expression|statement)+ ;

// A continuación los tokens (comienzan con mayúscula)
VAR : [a-z]+ ;
INT : [0-9]+ ;
STR : '"'(~[\r\n"] | '""')*'"';
WS : [ \t\n\r]+ -> skip ;
