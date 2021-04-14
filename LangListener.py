# Generated from Lang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#prog.
    def enterProg(self, ctx:LangParser.ProgContext):
        pass

    # Exit a parse tree produced by LangParser#prog.
    def exitProg(self, ctx:LangParser.ProgContext):
        pass


    # Enter a parse tree produced by LangParser#expr.
    def enterExpr(self, ctx:LangParser.ExprContext):
        pass

    # Exit a parse tree produced by LangParser#expr.
    def exitExpr(self, ctx:LangParser.ExprContext):
        pass


    # Enter a parse tree produced by LangParser#infixExpr.
    def enterInfixExpr(self, ctx:LangParser.InfixExprContext):
        pass

    # Exit a parse tree produced by LangParser#infixExpr.
    def exitInfixExpr(self, ctx:LangParser.InfixExprContext):
        pass


    # Enter a parse tree produced by LangParser#numberExpr.
    def enterNumberExpr(self, ctx:LangParser.NumberExprContext):
        pass

    # Exit a parse tree produced by LangParser#numberExpr.
    def exitNumberExpr(self, ctx:LangParser.NumberExprContext):
        pass


    # Enter a parse tree produced by LangParser#parensExpr.
    def enterParensExpr(self, ctx:LangParser.ParensExprContext):
        pass

    # Exit a parse tree produced by LangParser#parensExpr.
    def exitParensExpr(self, ctx:LangParser.ParensExprContext):
        pass


    # Enter a parse tree produced by LangParser#value.
    def enterValue(self, ctx:LangParser.ValueContext):
        pass

    # Exit a parse tree produced by LangParser#value.
    def exitValue(self, ctx:LangParser.ValueContext):
        pass


    # Enter a parse tree produced by LangParser#write.
    def enterWrite(self, ctx:LangParser.WriteContext):
        pass

    # Exit a parse tree produced by LangParser#write.
    def exitWrite(self, ctx:LangParser.WriteContext):
        pass


    # Enter a parse tree produced by LangParser#read.
    def enterRead(self, ctx:LangParser.ReadContext):
        pass

    # Exit a parse tree produced by LangParser#read.
    def exitRead(self, ctx:LangParser.ReadContext):
        pass


    # Enter a parse tree produced by LangParser#typ.
    def enterTyp(self, ctx:LangParser.TypContext):
        pass

    # Exit a parse tree produced by LangParser#typ.
    def exitTyp(self, ctx:LangParser.TypContext):
        pass


    # Enter a parse tree produced by LangParser#assign.
    def enterAssign(self, ctx:LangParser.AssignContext):
        pass

    # Exit a parse tree produced by LangParser#assign.
    def exitAssign(self, ctx:LangParser.AssignContext):
        pass


    # Enter a parse tree produced by LangParser#number.
    def enterNumber(self, ctx:LangParser.NumberContext):
        pass

    # Exit a parse tree produced by LangParser#number.
    def exitNumber(self, ctx:LangParser.NumberContext):
        pass



del LangParser