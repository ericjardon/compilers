from antlr.BasicVisitor import BasicVisitor
from antlr.BasicParser import BasicParser
from CodeGenerator import *
class EvalVisitor(BasicVisitor):
    memory = dict()

    def __init__(self, dataSegment) -> None:
        super().__init__()
        # Print the .data Segment
        printDataSegment(dataSegment)


    def visitAssign(self, ctx:BasicParser.AssignContext):
        # Triggered by initialization of values only.
        # Save (id:value) to internal memory
        id = ctx.ID().getText()
        value = int(self.INT().getText())
        self.memory[id] = value
        return value
    
    def visitReassign(self, ctx:BasicParser.ReassignContext):
        # Compute the value for assignment
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        printReAssignment(id, value)

    # Our language prints any expression
    def visitPrintExpr(self, ctx:BasicParser.PrintExprContext):
        value = self.visit(ctx.expr())  # returns literal value even if its label
        
        if isinstance(value, int):  # print immediate int
            printInti(value)
        else:
            # No Strings supported yet
            raise NotImplementedError
        
        return 0
    

    def visitId(self, ctx:BasicParser.IdContext):
        # If the id exists in memory return the value else return 0 (NULL)
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        else:
            return 0


    def visitINT(self, ctx:BasicParser.INTContext):
        return int(ctx.INT().getText())


    def visitMul(self, ctx:BasicParser.MulContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left * right
    
    
    def visitDiv(self, ctx:BasicParser.DivContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left // right


    def visitAdd(self, ctx:BasicParser.AddContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left + right
    
    
    def visitSub(self, ctx:BasicParser.SubContext):
        # Fetch left and right operands recursively
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left - right
    

    def visitParens(self, ctx:BasicParser.ParensContext):
        return self.visit(ctx.expr())
