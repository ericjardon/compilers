# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\antlr\eric.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ericParser import ericParser
else:
    from ericParser import ericParser

# This class defines a complete listener for a parse tree produced by ericParser.
class ericListener(ParseTreeListener):

    # Enter a parse tree produced by ericParser#let.
    def enterLet(self, ctx:ericParser.LetContext):
        pass

    # Exit a parse tree produced by ericParser#let.
    def exitLet(self, ctx:ericParser.LetContext):
        pass


    # Enter a parse tree produced by ericParser#show.
    def enterShow(self, ctx:ericParser.ShowContext):
        pass

    # Exit a parse tree produced by ericParser#show.
    def exitShow(self, ctx:ericParser.ShowContext):
        pass


    # Enter a parse tree produced by ericParser#expression.
    def enterExpression(self, ctx:ericParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ericParser#expression.
    def exitExpression(self, ctx:ericParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ericParser#statement.
    def enterStatement(self, ctx:ericParser.StatementContext):
        pass

    # Exit a parse tree produced by ericParser#statement.
    def exitStatement(self, ctx:ericParser.StatementContext):
        pass


    # Enter a parse tree produced by ericParser#program.
    def enterProgram(self, ctx:ericParser.ProgramContext):
        pass

    # Exit a parse tree produced by ericParser#program.
    def exitProgram(self, ctx:ericParser.ProgramContext):
        pass



del ericParser