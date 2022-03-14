# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\BasicMIPSCompiler\Basic\antlr\Basic.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete generic visitor for a parse tree produced by BasicParser.

class BasicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasicParser#prog.
    def visitProg(self, ctx:BasicParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#printExpr.
    def visitPrintExpr(self, ctx:BasicParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#assign.
    def visitAssign(self, ctx:BasicParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#reassign.
    def visitReassign(self, ctx:BasicParser.ReassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#blank.
    def visitBlank(self, ctx:BasicParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Div.
    def visitDiv(self, ctx:BasicParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Add.
    def visitAdd(self, ctx:BasicParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Sub.
    def visitSub(self, ctx:BasicParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#parens.
    def visitParens(self, ctx:BasicParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#Mul.
    def visitMul(self, ctx:BasicParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#id.
    def visitId(self, ctx:BasicParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#INT.
    def visitINT(self, ctx:BasicParser.INTContext):
        return self.visitChildren(ctx)



del BasicParser