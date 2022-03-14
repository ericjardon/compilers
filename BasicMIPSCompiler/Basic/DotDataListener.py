'''
Fetches all initializations in source code and generates the .data segment
'''
from antlr.BasicListener import BasicListener
from antlr.BasicParser import BasicParser

class DotDataListener(BasicListener):
    initial_values = dict() 

    # Assigment node corresponds to ID = INT
    def exitAssign(self, ctx:BasicParser.AssignContext):
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())

        self.initial_values[id] = value
    
    def exitReassign(self, ctx:BasicParser.ReassignContext):
        id = ctx.ID().getText()
        self.initial_values[id] = None
    
    def getDataSegment(self):
        return self.initial_values
