# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\antlr\eric.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ericParser import ericParser
else:
    from ericParser import ericParser

# This class defines a complete generic visitor for a parse tree produced by ericParser.

class ericVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ericParser#let.
    def visitLet(self, ctx:ericParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ericParser#show.
    def visitShow(self, ctx:ericParser.ShowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ericParser#expression.
    def visitExpression(self, ctx:ericParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ericParser#statement.
    def visitStatement(self, ctx:ericParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ericParser#program.
    def visitProgram(self, ctx:ericParser.ProgramContext):
        return self.visitChildren(ctx)



del ericParser