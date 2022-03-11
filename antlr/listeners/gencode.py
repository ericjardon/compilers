from antlr.ericListener import ericListener
from antlr.ericParser import ericParser

class GenCode(ericListener):
    
    def enterProgram(self, ctx:ericParser.ProgramContext):
        print(".text")

    def exitPrimaria(self, ctx:ericParser.PrimariaContext):
        print("load $1, " + ctx.Numero().getText())

    def exitSuma(self, ctx:ericParser.SumaContext):
        print("ADD")
