# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\BasicMIPSCompiler\Basic\antlr\Basic.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete listener for a parse tree produced by BasicParser.
class BasicListener(ParseTreeListener):

    # Enter a parse tree produced by BasicParser#prog.
    def enterProg(self, ctx:BasicParser.ProgContext):
        pass

    # Exit a parse tree produced by BasicParser#prog.
    def exitProg(self, ctx:BasicParser.ProgContext):
        pass


    # Enter a parse tree produced by BasicParser#printExpr.
    def enterPrintExpr(self, ctx:BasicParser.PrintExprContext):
        pass

    # Exit a parse tree produced by BasicParser#printExpr.
    def exitPrintExpr(self, ctx:BasicParser.PrintExprContext):
        pass


    # Enter a parse tree produced by BasicParser#assign.
    def enterAssign(self, ctx:BasicParser.AssignContext):
        pass

    # Exit a parse tree produced by BasicParser#assign.
    def exitAssign(self, ctx:BasicParser.AssignContext):
        pass


    # Enter a parse tree produced by BasicParser#reassign.
    def enterReassign(self, ctx:BasicParser.ReassignContext):
        pass

    # Exit a parse tree produced by BasicParser#reassign.
    def exitReassign(self, ctx:BasicParser.ReassignContext):
        pass


    # Enter a parse tree produced by BasicParser#blank.
    def enterBlank(self, ctx:BasicParser.BlankContext):
        pass

    # Exit a parse tree produced by BasicParser#blank.
    def exitBlank(self, ctx:BasicParser.BlankContext):
        pass


    # Enter a parse tree produced by BasicParser#Div.
    def enterDiv(self, ctx:BasicParser.DivContext):
        pass

    # Exit a parse tree produced by BasicParser#Div.
    def exitDiv(self, ctx:BasicParser.DivContext):
        pass


    # Enter a parse tree produced by BasicParser#Add.
    def enterAdd(self, ctx:BasicParser.AddContext):
        pass

    # Exit a parse tree produced by BasicParser#Add.
    def exitAdd(self, ctx:BasicParser.AddContext):
        pass


    # Enter a parse tree produced by BasicParser#Sub.
    def enterSub(self, ctx:BasicParser.SubContext):
        pass

    # Exit a parse tree produced by BasicParser#Sub.
    def exitSub(self, ctx:BasicParser.SubContext):
        pass


    # Enter a parse tree produced by BasicParser#parens.
    def enterParens(self, ctx:BasicParser.ParensContext):
        pass

    # Exit a parse tree produced by BasicParser#parens.
    def exitParens(self, ctx:BasicParser.ParensContext):
        pass


    # Enter a parse tree produced by BasicParser#Mul.
    def enterMul(self, ctx:BasicParser.MulContext):
        pass

    # Exit a parse tree produced by BasicParser#Mul.
    def exitMul(self, ctx:BasicParser.MulContext):
        pass


    # Enter a parse tree produced by BasicParser#id.
    def enterId(self, ctx:BasicParser.IdContext):
        pass

    # Exit a parse tree produced by BasicParser#id.
    def exitId(self, ctx:BasicParser.IdContext):
        pass


    # Enter a parse tree produced by BasicParser#INT.
    def enterINT(self, ctx:BasicParser.INTContext):
        pass

    # Exit a parse tree produced by BasicParser#INT.
    def exitINT(self, ctx:BasicParser.INTContext):
        pass



del BasicParser