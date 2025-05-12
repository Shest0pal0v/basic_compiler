# Generated from grammar/Basic.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete listener for a parse tree produced by BasicParser.
class BasicListener(ParseTreeListener):

    # Enter a parse tree produced by BasicParser#program.
    def enterProgram(self, ctx:BasicParser.ProgramContext):
        pass

    # Exit a parse tree produced by BasicParser#program.
    def exitProgram(self, ctx:BasicParser.ProgramContext):
        pass


    # Enter a parse tree produced by BasicParser#line.
    def enterLine(self, ctx:BasicParser.LineContext):
        pass

    # Exit a parse tree produced by BasicParser#line.
    def exitLine(self, ctx:BasicParser.LineContext):
        pass


    # Enter a parse tree produced by BasicParser#labelDef.
    def enterLabelDef(self, ctx:BasicParser.LabelDefContext):
        pass

    # Exit a parse tree produced by BasicParser#labelDef.
    def exitLabelDef(self, ctx:BasicParser.LabelDefContext):
        pass


    # Enter a parse tree produced by BasicParser#statement.
    def enterStatement(self, ctx:BasicParser.StatementContext):
        pass

    # Exit a parse tree produced by BasicParser#statement.
    def exitStatement(self, ctx:BasicParser.StatementContext):
        pass


    # Enter a parse tree produced by BasicParser#printStmt.
    def enterPrintStmt(self, ctx:BasicParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#printStmt.
    def exitPrintStmt(self, ctx:BasicParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#letStmt.
    def enterLetStmt(self, ctx:BasicParser.LetStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#letStmt.
    def exitLetStmt(self, ctx:BasicParser.LetStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#gotoStmt.
    def enterGotoStmt(self, ctx:BasicParser.GotoStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#gotoStmt.
    def exitGotoStmt(self, ctx:BasicParser.GotoStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#forStmt.
    def enterForStmt(self, ctx:BasicParser.ForStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#forStmt.
    def exitForStmt(self, ctx:BasicParser.ForStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#nextStmt.
    def enterNextStmt(self, ctx:BasicParser.NextStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#nextStmt.
    def exitNextStmt(self, ctx:BasicParser.NextStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#gosubStmt.
    def enterGosubStmt(self, ctx:BasicParser.GosubStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#gosubStmt.
    def exitGosubStmt(self, ctx:BasicParser.GosubStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#returnStmt.
    def enterReturnStmt(self, ctx:BasicParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#returnStmt.
    def exitReturnStmt(self, ctx:BasicParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#readStmt.
    def enterReadStmt(self, ctx:BasicParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#readStmt.
    def exitReadStmt(self, ctx:BasicParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#inputStmt.
    def enterInputStmt(self, ctx:BasicParser.InputStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#inputStmt.
    def exitInputStmt(self, ctx:BasicParser.InputStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#dimStmt.
    def enterDimStmt(self, ctx:BasicParser.DimStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#dimStmt.
    def exitDimStmt(self, ctx:BasicParser.DimStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#dataStmt.
    def enterDataStmt(self, ctx:BasicParser.DataStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#dataStmt.
    def exitDataStmt(self, ctx:BasicParser.DataStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#endStmt.
    def enterEndStmt(self, ctx:BasicParser.EndStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#endStmt.
    def exitEndStmt(self, ctx:BasicParser.EndStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#SingleIf.
    def enterSingleIf(self, ctx:BasicParser.SingleIfContext):
        pass

    # Exit a parse tree produced by BasicParser#SingleIf.
    def exitSingleIf(self, ctx:BasicParser.SingleIfContext):
        pass


    # Enter a parse tree produced by BasicParser#BlockIf.
    def enterBlockIf(self, ctx:BasicParser.BlockIfContext):
        pass

    # Exit a parse tree produced by BasicParser#BlockIf.
    def exitBlockIf(self, ctx:BasicParser.BlockIfContext):
        pass


    # Enter a parse tree produced by BasicParser#whileStmt.
    def enterWhileStmt(self, ctx:BasicParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#whileStmt.
    def exitWhileStmt(self, ctx:BasicParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#varRefList.
    def enterVarRefList(self, ctx:BasicParser.VarRefListContext):
        pass

    # Exit a parse tree produced by BasicParser#varRefList.
    def exitVarRefList(self, ctx:BasicParser.VarRefListContext):
        pass


    # Enter a parse tree produced by BasicParser#varRef.
    def enterVarRef(self, ctx:BasicParser.VarRefContext):
        pass

    # Exit a parse tree produced by BasicParser#varRef.
    def exitVarRef(self, ctx:BasicParser.VarRefContext):
        pass


    # Enter a parse tree produced by BasicParser#exprList.
    def enterExprList(self, ctx:BasicParser.ExprListContext):
        pass

    # Exit a parse tree produced by BasicParser#exprList.
    def exitExprList(self, ctx:BasicParser.ExprListContext):
        pass


    # Enter a parse tree produced by BasicParser#expression.
    def enterExpression(self, ctx:BasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BasicParser#expression.
    def exitExpression(self, ctx:BasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BasicParser#logicalExpr.
    def enterLogicalExpr(self, ctx:BasicParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by BasicParser#logicalExpr.
    def exitLogicalExpr(self, ctx:BasicParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by BasicParser#relationalExpr.
    def enterRelationalExpr(self, ctx:BasicParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by BasicParser#relationalExpr.
    def exitRelationalExpr(self, ctx:BasicParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by BasicParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:BasicParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by BasicParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:BasicParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by BasicParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:BasicParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by BasicParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:BasicParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by BasicParser#unaryExpr.
    def enterUnaryExpr(self, ctx:BasicParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by BasicParser#unaryExpr.
    def exitUnaryExpr(self, ctx:BasicParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by BasicParser#atom.
    def enterAtom(self, ctx:BasicParser.AtomContext):
        pass

    # Exit a parse tree produced by BasicParser#atom.
    def exitAtom(self, ctx:BasicParser.AtomContext):
        pass


    # Enter a parse tree produced by BasicParser#arrayRef.
    def enterArrayRef(self, ctx:BasicParser.ArrayRefContext):
        pass

    # Exit a parse tree produced by BasicParser#arrayRef.
    def exitArrayRef(self, ctx:BasicParser.ArrayRefContext):
        pass


    # Enter a parse tree produced by BasicParser#funcCall.
    def enterFuncCall(self, ctx:BasicParser.FuncCallContext):
        pass

    # Exit a parse tree produced by BasicParser#funcCall.
    def exitFuncCall(self, ctx:BasicParser.FuncCallContext):
        pass


    # Enter a parse tree produced by BasicParser#compOp.
    def enterCompOp(self, ctx:BasicParser.CompOpContext):
        pass

    # Exit a parse tree produced by BasicParser#compOp.
    def exitCompOp(self, ctx:BasicParser.CompOpContext):
        pass


    # Enter a parse tree produced by BasicParser#variable.
    def enterVariable(self, ctx:BasicParser.VariableContext):
        pass

    # Exit a parse tree produced by BasicParser#variable.
    def exitVariable(self, ctx:BasicParser.VariableContext):
        pass



del BasicParser