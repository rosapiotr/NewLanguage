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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("Q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\5\2\26\n\2\3\2\7\2\31\n\2\f\2")
        buf.write("\16\2\34\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4,\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\64\n\4\f\4\16\4\67\13\4\3\5\3\5\3\5\5\5<\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\2\3\6\13\2\4\6\b\n\f\16\20\22\2\6\3")
        buf.write("\2\17\20\3\2\r\16\3\2\5\7\3\2\21\22\2Q\2\32\3\2\2\2\4")
        buf.write("#\3\2\2\2\6+\3\2\2\2\b;\3\2\2\2\n=\3\2\2\2\fA\3\2\2\2")
        buf.write("\16H\3\2\2\2\20J\3\2\2\2\22N\3\2\2\2\24\26\5\4\3\2\25")
        buf.write("\24\3\2\2\2\25\26\3\2\2\2\26\27\3\2\2\2\27\31\7\24\2\2")
        buf.write("\30\25\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2")
        buf.write("\2\33\35\3\2\2\2\34\32\3\2\2\2\35\36\7\2\2\3\36\3\3\2")
        buf.write("\2\2\37$\5\6\4\2 $\5\n\6\2!$\5\f\7\2\"$\5\20\t\2#\37\3")
        buf.write("\2\2\2# \3\2\2\2#!\3\2\2\2#\"\3\2\2\2$\5\3\2\2\2%&\b\4")
        buf.write("\1\2&\'\7\3\2\2\'(\5\6\4\2()\7\4\2\2),\3\2\2\2*,\5\b\5")
        buf.write("\2+%\3\2\2\2+*\3\2\2\2,\65\3\2\2\2-.\f\5\2\2./\t\2\2\2")
        buf.write("/\64\5\6\4\6\60\61\f\4\2\2\61\62\t\3\2\2\62\64\5\6\4\5")
        buf.write("\63-\3\2\2\2\63\60\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2")
        buf.write("\65\66\3\2\2\2\66\7\3\2\2\2\67\65\3\2\2\28<\5\22\n\29")
        buf.write("<\7\13\2\2:<\7\f\2\2;8\3\2\2\2;9\3\2\2\2;:\3\2\2\2<\t")
        buf.write("\3\2\2\2=>\7\b\2\2>?\5\6\4\2?@\7\4\2\2@\13\3\2\2\2AB\7")
        buf.write("\13\2\2BC\7\n\2\2CD\7\t\2\2DE\7\3\2\2EF\5\16\b\2FG\7\4")
        buf.write("\2\2G\r\3\2\2\2HI\t\4\2\2I\17\3\2\2\2JK\7\13\2\2KL\7\n")
        buf.write("\2\2LM\5\6\4\2M\21\3\2\2\2NO\t\5\2\2O\23\3\2\2\2\t\25")
        buf.write("\32#+\63\65;")
        return buf.getvalue()


class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'int'", "'double'", "'str'", 
                     "'write('", "'read'", "'='", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INTEGER", 
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

    ruleNames =  [ "prog", "expr", "operation", "value", "write", "read", 
                   "typ", "assign", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INTEGER=3
    DOUBLE=4
    STR=5
    WRITE=6
    READ=7
    ASSIGN=8
    ID=9
    STRING=10
    OP_ADD=11
    OP_SUB=12
    OP_MUL=13
    OP_DIV=14
    INT=15
    REAL=16
    NUM=17
    NEWLINE=18
    WS=19

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
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LangParser.T__0) | (1 << LangParser.WRITE) | (1 << LangParser.ID) | (1 << LangParser.STRING) | (1 << LangParser.INT) | (1 << LangParser.REAL) | (1 << LangParser.NEWLINE))) != 0):
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LangParser.T__0) | (1 << LangParser.WRITE) | (1 << LangParser.ID) | (1 << LangParser.STRING) | (1 << LangParser.INT) | (1 << LangParser.REAL))) != 0):
                    self.state = 18
                    self.expr()


                self.state = 21
                self.match(LangParser.NEWLINE)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
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
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.operation(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.write()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.read()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.assign()
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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LangParser.T__0]:
                localctx = LangParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.match(LangParser.T__0)
                self.state = 37
                self.operation(0)
                self.state = 38
                self.match(LangParser.T__1)
                pass
            elif token in [LangParser.ID, LangParser.STRING, LangParser.INT, LangParser.REAL]:
                localctx = LangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.InfixExprContext(self, LangParser.OperationContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 43
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 44
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LangParser.OP_MUL or _la==LangParser.OP_DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        localctx.right = self.operation(4)
                        pass

                    elif la_ == 2:
                        localctx = LangParser.InfixExprContext(self, LangParser.OperationContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                        self.state = 46
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 47
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LangParser.OP_ADD or _la==LangParser.OP_SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        localctx.right = self.operation(3)
                        pass

             
                self.state = 53
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
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LangParser.INT, LangParser.REAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.number()
                pass
            elif token in [LangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(LangParser.ID)
                pass
            elif token in [LangParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
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
            self.state = 59
            self.match(LangParser.WRITE)
            self.state = 60
            self.operation(0)
            self.state = 61
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
            self.state = 63
            self.match(LangParser.ID)
            self.state = 64
            self.match(LangParser.ASSIGN)
            self.state = 65
            self.match(LangParser.READ)
            self.state = 66
            self.match(LangParser.T__0)
            self.state = 67
            self.typ()
            self.state = 68
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
            self.state = 70
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
            self.state = 72
            self.match(LangParser.ID)
            self.state = 73
            self.match(LangParser.ASSIGN)
            self.state = 74
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
            self.state = 76
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
         




