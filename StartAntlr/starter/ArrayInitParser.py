# Generated from c:\Users\ericj\Documents\ITESM-8\Compiladores\compiler-design\StartAntlr\starter\ArrayInit.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\26\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\7\2\13\n\2\f\2\16")
        buf.write("\2\16\13\2\3\2\3\2\3\3\3\3\5\3\24\n\3\3\3\2\2\4\2\4\2")
        buf.write("\2\2\25\2\6\3\2\2\2\4\23\3\2\2\2\6\7\7\3\2\2\7\f\5\4\3")
        buf.write("\2\b\t\7\4\2\2\t\13\5\4\3\2\n\b\3\2\2\2\13\16\3\2\2\2")
        buf.write("\f\n\3\2\2\2\f\r\3\2\2\2\r\17\3\2\2\2\16\f\3\2\2\2\17")
        buf.write("\20\7\5\2\2\20\3\3\2\2\2\21\24\5\2\2\2\22\24\7\6\2\2\23")
        buf.write("\21\3\2\2\2\23\22\3\2\2\2\24\5\3\2\2\2\4\f\23")
        return buf.getvalue()


class ArrayInitParser ( Parser ):

    grammarFileName = "ArrayInit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "WS" ]

    RULE_init = 0
    RULE_value = 1

    ruleNames =  [ "init", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INT=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArrayInitParser.ValueContext)
            else:
                return self.getTypedRuleContext(ArrayInitParser.ValueContext,i)


        def getRuleIndex(self):
            return ArrayInitParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = ArrayInitParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(ArrayInitParser.T__0)
            self.state = 5
            self.value()
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ArrayInitParser.T__1:
                self.state = 6
                self.match(ArrayInitParser.T__1)
                self.state = 7
                self.value()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 13
            self.match(ArrayInitParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init(self):
            return self.getTypedRuleContext(ArrayInitParser.InitContext,0)


        def INT(self):
            return self.getToken(ArrayInitParser.INT, 0)

        def getRuleIndex(self):
            return ArrayInitParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ArrayInitParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ArrayInitParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.init()
                pass
            elif token in [ArrayInitParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(ArrayInitParser.INT)
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





