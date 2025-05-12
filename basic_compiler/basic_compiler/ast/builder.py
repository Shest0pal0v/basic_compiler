from generated.BasicVisitor import BasicVisitor
from generated.BasicParser import BasicParser
from basic_compiler.ast.nodes import *

class ASTBuilder(BasicVisitor):

    def visitProgram(self, ctx: BasicParser.ProgramContext):
        stmts = []
        for line in ctx.line():
            if line.labelDef():
                stmts.append(self.visitLabelDef(line.labelDef()))
            elif line.statement():
                stmts.append(self.visit(line.statement()))
        return Program(stmts)

    def visitLabelDef(self, ctx: BasicParser.LabelDefContext):
        label_name = ctx.getText().rstrip(':')
        return Label(label_name)

    def visitLetStmt(self, ctx: BasicParser.LetStmtContext):
        name = ctx.variable().getText()
        expr = self.visit(ctx.expression())
        return Assign(name, expr)

    def visitPrintStmt(self, ctx: BasicParser.PrintStmtContext):
        if ctx.exprList():
            expr = ctx.exprList().expression(0)
            return Print(self.visit(expr))
        return Print(String(""))  # Пустая строка по умолчанию

    def visitGotoStmt(self, ctx: BasicParser.GotoStmtContext):
        tok = ctx.ID() or ctx.NUMBER()
        return Goto(tok.getText())

    def visitGosubStmt(self, ctx: BasicParser.GosubStmtContext):
        tok = ctx.ID() or ctx.NUMBER()
        return Gosub(tok.getText())

    def visitReturnStmt(self, ctx: BasicParser.ReturnStmtContext):
        return Return()

    def visitForStmt(self, ctx: BasicParser.ForStmtContext):
        var = Var(ctx.variable().getText())
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        step = self.visit(ctx.expression(2)) if ctx.STEP() else None
        return For(var, start, end, step)

    def visitNextStmt(self, ctx: BasicParser.NextStmtContext):
        vr = ctx.varRefList().varRef(0)
        if vr.variable():
            name = vr.variable().getText()
        else:
            name = vr.arrayRef().variable().getText()
        return Next(name)

    def visitSingleIf(self, ctx: BasicParser.SingleIfContext):
        cond = self.visit(ctx.expression(0))
        then_stmt = self.visit(ctx.statement(0)) if ctx.statement(0) else None
        else_stmt = self.visit(ctx.statement(1)) if ctx.ELSE() and ctx.statement(1) else None

        then_branch = [then_stmt] if then_stmt else []
        else_branch = [else_stmt] if else_stmt else []

        return If(cond, then_branch, else_branch)

    def visitBlockIf(self, ctx: BasicParser.BlockIfContext):
        cond = self.visit(ctx.expression(0))
        then_branch, else_branch = [], []
        current_branch = then_branch
        saw_else = False

        for line in ctx.line():
            txt = line.getText().strip().upper()
            if txt == 'ELSE':
                current_branch = else_branch
                saw_else = True
            elif line.statement():
                current_branch.append(self.visit(line.statement()))

        return If(cond, then_branch, else_branch if saw_else else [])

    def visitWhileStmt(self, ctx: BasicParser.WhileStmtContext):
        cond = self.visit(ctx.expression())
        body = [self.visit(ln.statement()) for ln in ctx.line() if ln.statement()]
        return While(cond, body)

    def visitReadStmt(self, ctx: BasicParser.ReadStmtContext):
        result = []
        for vr in ctx.varRefList().varRef():
            if vr.variable():
                result.append(Var(vr.variable().getText()))
            else:
                arr = vr.arrayRef()
                a = Var(arr.variable().getText())
                i = self.visit(arr.expression())
                result.append(ArrayRef(a, i))
        return Read(result)

    def visitInputStmt(self, ctx: BasicParser.InputStmtContext):
        prompt = ctx.STRING().getText() if ctx.STRING() else None
        result = []
        for vr in ctx.varRefList().varRef():
            if vr.variable():
                result.append(Var(vr.variable().getText()))
            else:
                arr = vr.arrayRef()
                a = Var(arr.variable().getText())
                i = self.visit(arr.expression())
                result.append(ArrayRef(a, i))
        return Input(prompt, result)

    def visitDimStmt(self, ctx: BasicParser.DimStmtContext):
        result = []
        for vr in ctx.varRefList().varRef():
            if vr.variable():
                result.append(Var(vr.variable().getText()))
            else:
                arr = vr.arrayRef()
                a = Var(arr.variable().getText())
                i = self.visit(arr.expression())
                result.append(ArrayRef(a, i))
        return Dim(result)

    def visitDataStmt(self, ctx: BasicParser.DataStmtContext):
        return Data([self.visit(e) for e in ctx.exprList().expression()])

    def visitEndStmt(self, ctx: BasicParser.EndStmtContext):
        return End()

    # --- Expressions ---

    def visitExpression(self, ctx: BasicParser.ExpressionContext):
        return self.visit(ctx.logicalExpr())

    def visitLogicalExpr(self, ctx: BasicParser.LogicalExprContext):
        node = self.visit(ctx.relationalExpr(0))
        for i in range(1, len(ctx.relationalExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.relationalExpr(i))
            node = BinOp(op, node, right)
        return node

    def visitRelationalExpr(self, ctx: BasicParser.RelationalExprContext):
        if ctx.compOp():
            left = self.visit(ctx.additiveExpr(0))
            right = self.visit(ctx.additiveExpr(1))
            return BinOp(ctx.compOp().getText(), left, right)
        return self.visit(ctx.additiveExpr(0))

    def visitAdditiveExpr(self, ctx: BasicParser.AdditiveExprContext):
        node = self.visit(ctx.multiplicativeExpr(0))
        for i in range(1, len(ctx.multiplicativeExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.multiplicativeExpr(i))
            node = BinOp(op, node, right)
        return node

    def visitMultiplicativeExpr(self, ctx: BasicParser.MultiplicativeExprContext):
        node = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.unaryExpr(i))
            node = BinOp(op, node, right)
        return node

    def visitUnaryExpr(self, ctx: BasicParser.UnaryExprContext):
        if ctx.MINUS():
            return BinOp('-', Number('0'), self.visit(ctx.atom()))
        return self.visit(ctx.atom())

    def visitAtom(self, ctx: BasicParser.AtomContext):
        if ctx.NUMBER():
            return Number(ctx.NUMBER().getText())
        if ctx.STRING():
            return String(ctx.STRING().getText())
        if ctx.arrayRef():
            arr = ctx.arrayRef()
            a = Var(arr.variable().getText())
            i = self.visit(arr.expression())
            return ArrayRef(a, i)
        if ctx.variable():
            return Var(ctx.variable().getText())
        if ctx.funcCall():
            return self.visit(ctx.funcCall())
        if ctx.expression():
            return self.visit(ctx.expression())

        raise Exception("Unknown atom context: " + ctx.getText())

    def visitFuncCall(self, ctx: BasicParser.FuncCallContext):
        args = [self.visit(e) for e in ctx.expression()]
        return FuncCall(ctx.FUNC().getText(), args)
