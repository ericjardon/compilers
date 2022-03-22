from antlr.basic2Listener import basic2Listener
from antlr.basic2Parser import basic2Parser

import asm

class GenCode(basic2Listener):
    def __init__(self):
        self.r = ''
        self.stack = []
    
    def enterProgram(self, ctx:basic2Parser.ProgramContext):
        self.r += asm.tpl_start_text
    
    def exitProgram(self, ctx: basic2Parser.ProgramContext):
        self.r += asm.tpl_end

    def exitPrimaria(self, ctx:basic2Parser.PrimariaContext):
        self.stack.append(
            asm.tpl_immediate.substitute(immediate=ctx.getText())
            )

    def exitSuma(self, ctx:basic2Parser.SumaContext):
        self.stack.append(
            asm.tpl_suma.substitute(
                right=self.stack.pop(), 
                left=self.stack.pop()
                )
            )

    def exitResta(self, ctx: basic2Parser.RestaContext):
        self.stack.append(
            asm.tpl_resta.substitute(
                right=self.stack.pop(), 
                left=self.stack.pop()
                )
            )
    def exitAsignacion(self, ctx: basic2Parser.AsignacionContext):
        self.r += asm.tpl_asignacion.substitute(
             prev=self.stack.pop(),
             name = ctx.getChild(0).getText()
        )
    
    def exitVar(self, ctx: basic2Parser.VarContext):
        self.stack.append(
            asm.tpl_var.substitute(name=ctx.getText())
        )
    
    def exitPrintint(self, ctx: basic2Parser.PrintintContext):
        self.r += asm.tpl_print_int.substitute(
            prev=self.stack.pop()
        )
