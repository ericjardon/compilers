# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\StartAntlr\Arith\antlr\Arith.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArithParser import ArithParser
else:
    from ArithParser import ArithParser

# This class defines a complete listener for a parse tree produced by ArithParser.
class ArithListener(ParseTreeListener):

    # Enter a parse tree produced by ArithParser#prog.
    def enterProg(self, ctx:ArithParser.ProgContext):
        pass

    # Exit a parse tree produced by ArithParser#prog.
    def exitProg(self, ctx:ArithParser.ProgContext):
        pass


    # Enter a parse tree produced by ArithParser#printExpr.
    def enterPrintExpr(self, ctx:ArithParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ArithParser#printExpr.
    def exitPrintExpr(self, ctx:ArithParser.PrintExprContext):
        pass


    # Enter a parse tree produced by ArithParser#assign.
    def enterAssign(self, ctx:ArithParser.AssignContext):
        pass

    # Exit a parse tree produced by ArithParser#assign.
    def exitAssign(self, ctx:ArithParser.AssignContext):
        pass


    # Enter a parse tree produced by ArithParser#blank.
    def enterBlank(self, ctx:ArithParser.BlankContext):
        pass

    # Exit a parse tree produced by ArithParser#blank.
    def exitBlank(self, ctx:ArithParser.BlankContext):
        pass


    # Enter a parse tree produced by ArithParser#parens.
    def enterParens(self, ctx:ArithParser.ParensContext):
        pass

    # Exit a parse tree produced by ArithParser#parens.
    def exitParens(self, ctx:ArithParser.ParensContext):
        pass


    # Enter a parse tree produced by ArithParser#MulDiv.
    def enterMulDiv(self, ctx:ArithParser.MulDivContext):
        pass

    # Exit a parse tree produced by ArithParser#MulDiv.
    def exitMulDiv(self, ctx:ArithParser.MulDivContext):
        pass


    # Enter a parse tree produced by ArithParser#AddSub.
    def enterAddSub(self, ctx:ArithParser.AddSubContext):
        pass

    # Exit a parse tree produced by ArithParser#AddSub.
    def exitAddSub(self, ctx:ArithParser.AddSubContext):
        pass


    # Enter a parse tree produced by ArithParser#id.
    def enterId(self, ctx:ArithParser.IdContext):
        pass

    # Exit a parse tree produced by ArithParser#id.
    def exitId(self, ctx:ArithParser.IdContext):
        pass


    # Enter a parse tree produced by ArithParser#INT.
    def enterINT(self, ctx:ArithParser.INTContext):
        pass

    # Exit a parse tree produced by ArithParser#INT.
    def exitINT(self, ctx:ArithParser.INTContext):
        pass



del ArithParser