# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\antlr\eric.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\30\n\4\3\4\3\4\3")
        buf.write("\4\7\4\35\n\4\f\4\16\4 \13\4\3\5\3\5\5\5$\n\5\3\6\3\6")
        buf.write("\6\6(\n\6\r\6\16\6)\3\6\2\3\6\7\2\4\6\b\n\2\4\3\2\7\b")
        buf.write("\3\2\6\b\2,\2\f\3\2\2\2\4\20\3\2\2\2\6\27\3\2\2\2\b#\3")
        buf.write("\2\2\2\n\'\3\2\2\2\f\r\7\6\2\2\r\16\7\3\2\2\16\17\t\2")
        buf.write("\2\2\17\3\3\2\2\2\20\21\7\4\2\2\21\22\t\3\2\2\22\5\3\2")
        buf.write("\2\2\23\24\b\4\1\2\24\30\7\7\2\2\25\30\7\b\2\2\26\30\7")
        buf.write("\6\2\2\27\23\3\2\2\2\27\25\3\2\2\2\27\26\3\2\2\2\30\36")
        buf.write("\3\2\2\2\31\32\f\6\2\2\32\33\7\5\2\2\33\35\5\6\4\7\34")
        buf.write("\31\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37")
        buf.write("\7\3\2\2\2 \36\3\2\2\2!$\5\2\2\2\"$\5\4\3\2#!\3\2\2\2")
        buf.write("#\"\3\2\2\2$\t\3\2\2\2%(\5\6\4\2&(\5\b\5\2\'%\3\2\2\2")
        buf.write("\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\13\3\2\2\2")
        buf.write("\7\27\36#\')")
        return buf.getvalue()


class ericParser ( Parser ):

    grammarFileName = "eric.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'show'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "INT", "STR", "WS" ]

    RULE_let = 0
    RULE_show = 1
    RULE_expression = 2
    RULE_statement = 3
    RULE_program = 4

    ruleNames =  [ "let", "show", "expression", "statement", "program" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VAR=4
    INT=5
    STR=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ericParser.VAR, 0)

        def INT(self):
            return self.getToken(ericParser.INT, 0)

        def STR(self):
            return self.getToken(ericParser.STR, 0)

        def getRuleIndex(self):
            return ericParser.RULE_let

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)




    def let(self):

        localctx = ericParser.LetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_let)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(ericParser.VAR)
            self.state = 11
            self.match(ericParser.T__0)
            self.state = 12
            _la = self._input.LA(1)
            if not(_la==ericParser.INT or _la==ericParser.STR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ericParser.INT, 0)

        def STR(self):
            return self.getToken(ericParser.STR, 0)

        def VAR(self):
            return self.getToken(ericParser.VAR, 0)

        def getRuleIndex(self):
            return ericParser.RULE_show

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow" ):
                listener.enterShow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow" ):
                listener.exitShow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShow" ):
                return visitor.visitShow(self)
            else:
                return visitor.visitChildren(self)




    def show(self):

        localctx = ericParser.ShowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_show)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(ericParser.T__1)
            self.state = 15
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ericParser.VAR) | (1 << ericParser.INT) | (1 << ericParser.STR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def INT(self):
            return self.getToken(ericParser.INT, 0)

        def STR(self):
            return self.getToken(ericParser.STR, 0)

        def VAR(self):
            return self.getToken(ericParser.VAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ericParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ericParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ericParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ericParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ericParser.INT]:
                self.state = 18
                self.match(ericParser.INT)
                pass
            elif token in [ericParser.STR]:
                self.state = 19
                self.match(ericParser.STR)
                pass
            elif token in [ericParser.VAR]:
                self.state = 20
                self.match(ericParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ericParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 23
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 24
                    self.match(ericParser.T__2)
                    self.state = 25
                    self.expression(5) 
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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

        def let(self):
            return self.getTypedRuleContext(ericParser.LetContext,0)


        def show(self):
            return self.getTypedRuleContext(ericParser.ShowContext,0)


        def getRuleIndex(self):
            return ericParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ericParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ericParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.let()
                pass
            elif token in [ericParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.show()
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


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ericParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ericParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ericParser.StatementContext)
            else:
                return self.getTypedRuleContext(ericParser.StatementContext,i)


        def getRuleIndex(self):
            return ericParser.RULE_program

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

        localctx = ericParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 36
                    self.statement()
                    pass


                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ericParser.T__1) | (1 << ericParser.VAR) | (1 << ericParser.INT) | (1 << ericParser.STR))) != 0)):
                    break

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
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




