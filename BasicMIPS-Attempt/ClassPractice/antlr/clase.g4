grammar clase;

program : expression+ | statement+;

expression:
    expression '+' expression #suma
    | Number                  #Number
    | 