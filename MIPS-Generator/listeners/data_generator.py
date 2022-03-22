from antlr.basic2Listener import basic2Listener
from antlr.basic2Parser import basic2Parser

import asm

class DataGenerator(basic2Listener):
    def __init__(self):
        self.r = ''

    def enterProgram(self, ctx: basic2Parser.ProgramContext):
        self.r += asm.tpl_start_data

    def enterDeclaracion(self, ctx: basic2Parser.DeclaracionContext):
        self.r += asm.tpl_var_decl.substitute(
            varname = ctx.getChild(1).getText()
            )