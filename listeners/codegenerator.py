from tkinter import Variable
from antlr.ericListener import ericListener
from antlr.ericParser import ericParser

class CodeGenerator(ericListener):

    variables = dict()
    
    # Action of show
    def exitShow(self, ctx:ericParser.ShowContext):
        if (ctx.INT() is not None):
            print(ctx.INT().getText())
        elif (ctx.STR() is not None):
            print(ctx.STR().getText())
        
        elif (ctx.VAR() is not None):
            print(
                self.variables[ctx.VAR().getText()]
                )

    # Action of let
    def exitLet(self, ctx:ericParser.LetContext):
        if ctx.INT() is not None:
            value = int(ctx.INT().getText())
        else:
            value = ctx.STR().getText()

        self.variables[ctx.VAR().getText()] = value
