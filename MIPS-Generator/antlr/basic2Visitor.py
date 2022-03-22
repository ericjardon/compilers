# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\MIPS-Generator\antlr\basic2.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .basic2Parser import basic2Parser
else:
    from basic2Parser import basic2Parser

# This class defines a complete generic visitor for a parse tree produced by basic2Parser.

class basic2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by basic2Parser#program.
    def visitProgram(self, ctx:basic2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basic2Parser#suma.
    def visitSuma(self, ctx:basic2Parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basic2Parser#parens.
    def visitParens(self, ctx:basic2Parser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basic2Parser#var.
    def visitVar(self, ctx:basic2Parser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basic2Parser#primaria.
    def visitPrimaria(self, ctx:basic2Parser.PrimariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basic2Parser#resta.
    def visitResta(self, ctx:basic2Parser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basic2Parser#declaracion.
    def visitDeclaracion(self, ctx:basic2Parser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basic2Parser#asignacion.
    def visitAsignacion(self, ctx:basic2Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basic2Parser#printint.
    def visitPrintint(self, ctx:basic2Parser.PrintintContext):
        return self.visitChildren(ctx)



del basic2Parser