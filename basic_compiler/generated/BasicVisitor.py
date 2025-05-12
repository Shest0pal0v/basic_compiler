# Generated from grammar/Basic.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete generic visitor for a parse tree produced by BasicParser.

class BasicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasicParser#program.
    def visitProgram(self, ctx:BasicParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#line.
    def visitLine(self, ctx:BasicParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#labelDef.
    def visitLabelDef(self, ctx:BasicParser.LabelDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#statement.
    def visitStatement(self, ctx:BasicParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#printStmt.
    def visitPrintStmt(self, ctx:BasicParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#letStmt.
    def visitLetStmt(self, ctx:BasicParser.LetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#gotoStmt.
    def visitGotoStmt(self, ctx:BasicParser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#forStmt.
    def visitForStmt(self, ctx:BasicParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#nextStmt.
    def visitNextStmt(self, ctx:BasicParser.NextStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#gosubStmt.
    def visitGosubStmt(self, ctx:BasicParser.GosubStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#returnStmt.
    def visitReturnStmt(self, ctx:BasicParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#readStmt.
    def visitReadStmt(self, ctx:BasicParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#inputStmt.
    def visitInputStmt(self, ctx:BasicParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#dimStmt.
    def visitDimStmt(self, ctx:BasicParser.DimStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#dataStmt.
    def visitDataStmt(self, ctx:BasicParser.DataStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#endStmt.
    def visitEndStmt(self, ctx:BasicParser.EndStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#SingleIf.
    def visitSingleIf(self, ctx:BasicParser.SingleIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#BlockIf.
    def visitBlockIf(self, ctx:BasicParser.BlockIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#whileStmt.
    def visitWhileStmt(self, ctx:BasicParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#varRefList.
    def visitVarRefList(self, ctx:BasicParser.VarRefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#varRef.
    def visitVarRef(self, ctx:BasicParser.VarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#exprList.
    def visitExprList(self, ctx:BasicParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#expression.
    def visitExpression(self, ctx:BasicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#logicalExpr.
    def visitLogicalExpr(self, ctx:BasicParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#relationalExpr.
    def visitRelationalExpr(self, ctx:BasicParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:BasicParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:BasicParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#unaryExpr.
    def visitUnaryExpr(self, ctx:BasicParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#atom.
    def visitAtom(self, ctx:BasicParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#arrayRef.
    def visitArrayRef(self, ctx:BasicParser.ArrayRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#funcCall.
    def visitFuncCall(self, ctx:BasicParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#compOp.
    def visitCompOp(self, ctx:BasicParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicParser#variable.
    def visitVariable(self, ctx:BasicParser.VariableContext):
        return self.visitChildren(ctx)



del BasicParser