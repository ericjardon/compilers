from antlr.ArithVisitor import ArithVisitor
from antlr.ArithParser import ArithParser

class EvalVisitor(ArithVisitor):
    memory = dict()

    @Override
    def visitAssign(self, ctx:ArithParser.AssignContext):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        
        return value

    @Override
    def visitPrintExpr(self, ctx:ArithParser.PrintExprContext):
        value = self.visit(ctx.expr())  # evaluate expr child
        print(value)
        return 0 # dummy return value

    # CONTINUE: PAGE 37