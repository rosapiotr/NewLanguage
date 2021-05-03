# Generated from Lang.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\5\2\32\n\2")
        buf.write("\3\2\7\2\35\n\2\f\2\16\2 \13\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3)\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\61\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\7\49\n\4\f\4\16\4<\13\4\3\5\3\5\3\5")
        buf.write("\5\5A\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13]\n\13\3\13\7\13`\n\13\f\13\16\13c\13")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\2\3\6\r\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\2\7\3\2\27\30\3\2\25\26\3\2\r\17\3\2\31\32\3\2")
        buf.write("\b\f\2j\2\36\3\2\2\2\4(\3\2\2\2\6\60\3\2\2\2\b@\3\2\2")
        buf.write("\2\nB\3\2\2\2\fF\3\2\2\2\16M\3\2\2\2\20O\3\2\2\2\22S\3")
        buf.write("\2\2\2\24U\3\2\2\2\26f\3\2\2\2\30\32\5\4\3\2\31\30\3\2")
        buf.write("\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33\35\7\34\2\2\34\31")
        buf.write("\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37!\3")
        buf.write("\2\2\2 \36\3\2\2\2!\"\7\2\2\3\"\3\3\2\2\2#)\5\6\4\2$)")
        buf.write("\5\n\6\2%)\5\f\7\2&)\5\20\t\2\')\5\24\13\2(#\3\2\2\2(")
        buf.write("$\3\2\2\2(%\3\2\2\2(&\3\2\2\2(\'\3\2\2\2)\5\3\2\2\2*+")
        buf.write("\b\4\1\2+,\7\3\2\2,-\5\6\4\2-.\7\4\2\2.\61\3\2\2\2/\61")
        buf.write("\5\b\5\2\60*\3\2\2\2\60/\3\2\2\2\61:\3\2\2\2\62\63\f\5")
        buf.write("\2\2\63\64\t\2\2\2\649\5\6\4\6\65\66\f\4\2\2\66\67\t\3")
        buf.write("\2\2\679\5\6\4\58\62\3\2\2\28\65\3\2\2\29<\3\2\2\2:8\3")
        buf.write("\2\2\2:;\3\2\2\2;\7\3\2\2\2<:\3\2\2\2=A\5\22\n\2>A\7\23")
        buf.write("\2\2?A\7\24\2\2@=\3\2\2\2@>\3\2\2\2@?\3\2\2\2A\t\3\2\2")
        buf.write("\2BC\7\20\2\2CD\5\6\4\2DE\7\4\2\2E\13\3\2\2\2FG\7\23\2")
        buf.write("\2GH\7\22\2\2HI\7\21\2\2IJ\7\3\2\2JK\5\16\b\2KL\7\4\2")
        buf.write("\2L\r\3\2\2\2MN\t\4\2\2N\17\3\2\2\2OP\7\23\2\2PQ\7\22")
        buf.write("\2\2QR\5\6\4\2R\21\3\2\2\2ST\t\5\2\2T\23\3\2\2\2UV\7\7")
        buf.write("\2\2VW\5\b\5\2WX\5\26\f\2XY\5\b\5\2YZ\7\4\2\2Za\7\5\2")
        buf.write("\2[]\5\4\3\2\\[\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^`\7\34\2")
        buf.write("\2_\\\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2")
        buf.write("ca\3\2\2\2de\7\6\2\2e\25\3\2\2\2fg\t\6\2\2g\27\3\2\2\2")
        buf.write("\13\31\36(\608:@\\a")
        return buf.getvalue()


class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'if('", "'>='", 
                     "'<='", "'>'", "'<'", "'=='", "'int'", "'double'", 
                     "'str'", "'write('", "'read'", "'='", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IF", "GE", "LE", "GT", "LT", "EQ", "INTEGER", 
                      "DOUBLE", "STR", "WRITE", "READ", "ASSIGN", "ID", 
                      "STRING", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", 
                      "INT", "REAL", "NUM", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_operation = 2
    RULE_value = 3
    RULE_write = 4
    RULE_read = 5
    RULE_typ = 6
    RULE_assign = 7
    RULE_number = 8
    RULE_ifExpr = 9
    RULE_comp = 10

    ruleNames =  [ "prog", "expr", "operation", "value", "write", "read", 
                   "typ", "assign", "number", "ifExpr", "comp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IF=5
    GE=6
    LE=7
    GT=8
    LT=9
    EQ=10
    INTEGER=11
    DOUBLE=12
    STR=13
    WRITE=14
    READ=15
    ASSIGN=16
    ID=17
    STRING=18
    OP_ADD=19
    OP_SUB=20
    OP_MUL=21
    OP_DIV=22
    INT=23
    REAL=24
    NUM=25
    NEWLINE=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LangParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.NEWLINE)
            else:
                return self.getToken(LangParser.NEWLINE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = LangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LangParser.T__0) | (1 << LangParser.IF) | (1 << LangParser.WRITE) | (1 << LangParser.ID) | (1 << LangParser.STRING) | (1 << LangParser.INT) | (1 << LangParser.REAL) | (1 << LangParser.NEWLINE))) != 0):
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LangParser.T__0) | (1 << LangParser.IF) | (1 << LangParser.WRITE) | (1 << LangParser.ID) | (1 << LangParser.STRING) | (1 << LangParser.INT) | (1 << LangParser.REAL))) != 0):
                    self.state = 22
                    self.expr()


                self.state = 25
                self.match(LangParser.NEWLINE)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(LangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(LangParser.OperationContext,0)


        def write(self):
            return self.getTypedRuleContext(LangParser.WriteContext,0)


        def read(self):
            return self.getTypedRuleContext(LangParser.ReadContext,0)


        def assign(self):
            return self.getTypedRuleContext(LangParser.AssignContext,0)


        def ifExpr(self):
            return self.getTypedRuleContext(LangParser.IfExprContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = LangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.operation(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.write()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.read()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.assign()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.ifExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LangParser.RULE_operation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class InfixExprContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.OperationContext
            super().__init__(parser)
            self.left = None # OperationContext
            self.op = None # Token
            self.right = None # OperationContext
            self.copyFrom(ctx)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.OperationContext)
            else:
                return self.getTypedRuleContext(LangParser.OperationContext,i)

        def OP_MUL(self):
            return self.getToken(LangParser.OP_MUL, 0)
        def OP_DIV(self):
            return self.getToken(LangParser.OP_DIV, 0)
        def OP_ADD(self):
            return self.getToken(LangParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(LangParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)


    class NumberExprContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(LangParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)


    class ParensExprContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operation(self):
            return self.getTypedRuleContext(LangParser.OperationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)



    def operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.OperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LangParser.T__0]:
                localctx = LangParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(LangParser.T__0)
                self.state = 42
                self.operation(0)
                self.state = 43
                self.match(LangParser.T__1)
                pass
            elif token in [LangParser.ID, LangParser.STRING, LangParser.INT, LangParser.REAL]:
                localctx = LangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.InfixExprContext(self, LangParser.OperationContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 48
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 49
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LangParser.OP_MUL or _la==LangParser.OP_DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        localctx.right = self.operation(4)
                        pass

                    elif la_ == 2:
                        localctx = LangParser.InfixExprContext(self, LangParser.OperationContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 51
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LangParser.OP_ADD or _la==LangParser.OP_SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        localctx.right = self.operation(3)
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(LangParser.NumberContext,0)


        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def STRING(self):
            return self.getToken(LangParser.STRING, 0)

        def getRuleIndex(self):
            return LangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = LangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LangParser.INT, LangParser.REAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.number()
                pass
            elif token in [LangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(LangParser.ID)
                pass
            elif token in [LangParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(LangParser.STRING)
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


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(LangParser.WRITE, 0)

        def operation(self):
            return self.getTypedRuleContext(LangParser.OperationContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)




    def write(self):

        localctx = LangParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(LangParser.WRITE)
            self.state = 65
            self.operation(0)
            self.state = 66
            self.match(LangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(LangParser.ASSIGN, 0)

        def READ(self):
            return self.getToken(LangParser.READ, 0)

        def typ(self):
            return self.getTypedRuleContext(LangParser.TypContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = LangParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(LangParser.ID)
            self.state = 69
            self.match(LangParser.ASSIGN)
            self.state = 70
            self.match(LangParser.READ)
            self.state = 71
            self.match(LangParser.T__0)
            self.state = 72
            self.typ()
            self.state = 73
            self.match(LangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(LangParser.INTEGER, 0)

        def DOUBLE(self):
            return self.getToken(LangParser.DOUBLE, 0)

        def STR(self):
            return self.getToken(LangParser.STR, 0)

        def getRuleIndex(self):
            return LangParser.RULE_typ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)




    def typ(self):

        localctx = LangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LangParser.INTEGER) | (1 << LangParser.DOUBLE) | (1 << LangParser.STR))) != 0)):
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(LangParser.ASSIGN, 0)

        def operation(self):
            return self.getTypedRuleContext(LangParser.OperationContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = LangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(LangParser.ID)
            self.state = 78
            self.match(LangParser.ASSIGN)
            self.state = 79
            self.operation(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LangParser.INT, 0)

        def REAL(self):
            return self.getToken(LangParser.REAL, 0)

        def getRuleIndex(self):
            return LangParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = LangParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==LangParser.INT or _la==LangParser.REAL):
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


    class IfExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ValueContext
            self.right = None # ValueContext

        def IF(self):
            return self.getToken(LangParser.IF, 0)

        def comp(self):
            return self.getTypedRuleContext(LangParser.CompContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ValueContext)
            else:
                return self.getTypedRuleContext(LangParser.ValueContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.NEWLINE)
            else:
                return self.getToken(LangParser.NEWLINE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_ifExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr" ):
                listener.enterIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr" ):
                listener.exitIfExpr(self)




    def ifExpr(self):

        localctx = LangParser.IfExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(LangParser.IF)
            self.state = 84
            localctx.left = self.value()
            self.state = 85
            self.comp()
            self.state = 86
            localctx.right = self.value()
            self.state = 87
            self.match(LangParser.T__1)
            self.state = 88
            self.match(LangParser.T__2)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LangParser.T__0) | (1 << LangParser.IF) | (1 << LangParser.WRITE) | (1 << LangParser.ID) | (1 << LangParser.STRING) | (1 << LangParser.INT) | (1 << LangParser.REAL) | (1 << LangParser.NEWLINE))) != 0):
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LangParser.T__0) | (1 << LangParser.IF) | (1 << LangParser.WRITE) | (1 << LangParser.ID) | (1 << LangParser.STRING) | (1 << LangParser.INT) | (1 << LangParser.REAL))) != 0):
                    self.state = 89
                    self.expr()


                self.state = 92
                self.match(LangParser.NEWLINE)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(LangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GE(self):
            return self.getToken(LangParser.GE, 0)

        def LE(self):
            return self.getToken(LangParser.LE, 0)

        def GT(self):
            return self.getToken(LangParser.GT, 0)

        def LT(self):
            return self.getToken(LangParser.LT, 0)

        def EQ(self):
            return self.getToken(LangParser.EQ, 0)

        def getRuleIndex(self):
            return LangParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = LangParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LangParser.GE) | (1 << LangParser.LE) | (1 << LangParser.GT) | (1 << LangParser.LT) | (1 << LangParser.EQ))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.operation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def operation_sempred(self, localctx:OperationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




