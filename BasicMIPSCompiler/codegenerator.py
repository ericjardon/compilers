from tkinter import Variable
from antlr.ericListener import ericListener
from antlr.ericParser import ericParser
from collections import deque
class CodeGenerator(ericListener):

    variables = dict()
    stack = deque()
    
    # Action of show
    def exitShow(self, ctx:ericParser.ShowContext):
        if (ctx.INT() is not None):
            print(ctx.INT().getText())
        
        elif (ctx.VAR() is not None):
            print(
                self.variables[ctx.VAR().getText()]
                )

    # Action of let: do assignment
    def exitAssign(self, ctx:ericParser.LetContext):
        # INT ya está cargada
        value = int(ctx.INT().getText())
        self.variables[ctx.VAR().getText()] = value

    def exitOperand(self, ctx:ericParser.OperandContext):
    # Obten el tipo de operación
    # imprime lw t0 y t1, guardados en los dos primeros lugares de la pila
    # y luego la directiva correspondiente
        if ctx.ADD() is not None:
            # pop twice from stack
            name1 = self.stack.pop()
            name2 = self.stack.pop()
            
            print(f'lw $t0, {name1}')
            print(f'lw $t1, {name1}')
            print('add $t2, $t1, $t0')

            self.stack.push(self.variables[name1] + self.variables[name2])
