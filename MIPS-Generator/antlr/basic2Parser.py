# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\MIPS-Generator\antlr\basic2.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\25\n\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4,\n\4\3\4\2\3\4\5\2\4\6\2\2\2")
        buf.write("\61\2\t\3\2\2\2\4\24\3\2\2\2\6+\3\2\2\2\b\n\5\6\4\2\t")
        buf.write("\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3")
        buf.write("\3\2\2\2\r\16\b\3\1\2\16\17\7\5\2\2\17\20\5\4\3\2\20\21")
        buf.write("\7\6\2\2\21\25\3\2\2\2\22\25\7\n\2\2\23\25\7\13\2\2\24")
        buf.write("\r\3\2\2\2\24\22\3\2\2\2\24\23\3\2\2\2\25\36\3\2\2\2\26")
        buf.write("\27\f\7\2\2\27\30\7\3\2\2\30\35\5\4\3\b\31\32\f\6\2\2")
        buf.write("\32\33\7\4\2\2\33\35\5\4\3\7\34\26\3\2\2\2\34\31\3\2\2")
        buf.write("\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37\5\3\2\2")
        buf.write("\2 \36\3\2\2\2!\"\7\7\2\2\",\7\13\2\2#$\7\13\2\2$%\7\b")
        buf.write("\2\2%,\5\4\3\2&\'\7\t\2\2\'(\7\5\2\2()\5\4\3\2)*\7\6\2")
        buf.write("\2*,\3\2\2\2+!\3\2\2\2+#\3\2\2\2+&\3\2\2\2,\7\3\2\2\2")
        buf.write("\7\13\24\34\36+")
        return buf.getvalue()


class basic2Parser ( Parser ):

    grammarFileName = "basic2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'('", "')'", "'int'", "'='", 
                     "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Numero", "Variable", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Numero=8
    Variable=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basic2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(basic2Parser.StatementContext,i)


        def getRuleIndex(self):
            return basic2Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = basic2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.statement()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << basic2Parser.T__4) | (1 << basic2Parser.T__6) | (1 << basic2Parser.Variable))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return basic2Parser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basic2Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basic2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basic2Parser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basic2Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(basic2Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basic2Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(basic2Parser.Variable, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class PrimariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basic2Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(basic2Parser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaria" ):
                return visitor.visitPrimaria(self)
            else:
                return visitor.visitChildren(self)


    class RestaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basic2Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basic2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basic2Parser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResta" ):
                listener.enterResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResta" ):
                listener.exitResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = basic2Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [basic2Parser.T__2]:
                localctx = basic2Parser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.match(basic2Parser.T__2)
                self.state = 13
                self.expression(0)
                self.state = 14
                self.match(basic2Parser.T__3)
                pass
            elif token in [basic2Parser.Numero]:
                localctx = basic2Parser.PrimariaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(basic2Parser.Numero)
                pass
            elif token in [basic2Parser.Variable]:
                localctx = basic2Parser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(basic2Parser.Variable)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 26
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = basic2Parser.SumaContext(self, basic2Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 20
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 21
                        self.match(basic2Parser.T__0)
                        self.state = 22
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = basic2Parser.RestaContext(self, basic2Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 23
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 24
                        self.match(basic2Parser.T__1)
                        self.state = 25
                        self.expression(5)
                        pass

             
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return basic2Parser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basic2Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(basic2Parser.Variable, 0)
        def expression(self):
            return self.getTypedRuleContext(basic2Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basic2Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Variable(self):
            return self.getToken(basic2Parser.Variable, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)


    class PrintintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basic2Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(basic2Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintint" ):
                listener.enterPrintint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintint" ):
                listener.exitPrintint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintint" ):
                return visitor.visitPrintint(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = basic2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [basic2Parser.T__4]:
                localctx = basic2Parser.DeclaracionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(basic2Parser.T__4)
                self.state = 32
                self.match(basic2Parser.Variable)
                pass
            elif token in [basic2Parser.Variable]:
                localctx = basic2Parser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(basic2Parser.Variable)
                self.state = 34
                self.match(basic2Parser.T__5)
                self.state = 35
                self.expression(0)
                pass
            elif token in [basic2Parser.T__6]:
                localctx = basic2Parser.PrintintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(basic2Parser.T__6)
                self.state = 37
                self.match(basic2Parser.T__2)
                self.state = 38
                self.expression(0)
                self.state = 39
                self.match(basic2Parser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




