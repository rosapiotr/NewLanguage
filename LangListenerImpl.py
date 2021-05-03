from llvm_generator import LLVMGenerator
from LangListener import LangListener
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

import sys

class LangListenerImpl(LangListener):
    def __init__(self):
        self.variables = dict()
        self.stack = []
        self.operation_types = []

    def error(self, line, message):
       print("Error, line " + str(line) + ", " + message)
       sys.exit(1)

    def exitRead(self, ctx:LangParser.ReadContext):
        id = ctx.ID().getText()
        typ = ctx.typ().getText()
        if typ == "double": typ = "float"
        if id in self.variables.keys() and self.variables[id] != typ:
            self.error(ctx.start.line, "Redefinition of type of variable " + id)
        if id not in self.variables.keys():
            if typ == "float":
                LLVMGenerator.declare_float(id)
            elif typ == "int":
                LLVMGenerator.declare_i32(id)
            elif typ == "str":
                typ = "strs"
            self.variables[id] = typ
        LLVMGenerator.read_value(id, typ)

    def exitWrite(self, ctx:LangParser.WriteContext):
        if ctx.operation() is not None:
            v = self.stack.pop()
            v_type = self.stack.pop()

            if v_type == "ID":
                if v not in self.variables.keys():
                    self.error(ctx.start.line, "Variable has not been declared: " + v)
                LLVMGenerator.print_id(v, self.variables[v])
            elif v_type == "float":
                LLVMGenerator.declare_assign_float(v)
            elif v_type == "int":
                LLVMGenerator.declare_assign_i32(v)
            elif v_type == "str":
                LLVMGenerator.declare_assign_string(v)
            LLVMGenerator.print_id(str(LLVMGenerator.reg-1), v_type)
            self.operation_types = []

    def exitInfixExpr(self, ctx:LangParser.InfixExprContext):
        v2 = self.stack.pop()
        v2_type = self.stack.pop()
        v1 = self.stack.pop()
        v1_type = self.stack.pop()
        values = []

        if v2_type == "ID":
            LLVMGenerator.withdraw_id(v2, self.variables[v2])
            if self.variables[v2] == "int":
                if v1_type == "float" or (v1 in self.variables.keys() and self.variables[v1] == "float"):
                    LLVMGenerator.convert_to_float()
        elif v2_type == "int":
            LLVMGenerator.declare_assign_i32(v2)
            if v1_type == "float" or (v1 in self.variables.keys() and self.variables[v1] == "float") or "float" in self.operation_types:
                LLVMGenerator.withdraw_last("int")
                LLVMGenerator.convert_to_float()
            else:
                LLVMGenerator.withdraw_last("int")
        elif v2_type == "float":
            LLVMGenerator.declare_assign_float(v2)
            LLVMGenerator.withdraw_last("float")
        values.append("%"+str(LLVMGenerator.reg-1))

        if v1_type == "ID":
            LLVMGenerator.withdraw_id(v1, self.variables[v1])
            if self.variables[v1] == "int":
                if v2_type == "float" or (v2 in self.variables.keys() and self.variables[v2] == "float"):
                    LLVMGenerator.convert_to_float()
        elif v1_type == "int":
            LLVMGenerator.declare_assign_i32(v1)
            if v2_type == "float" or (v2 in self.variables.keys() and self.variables[v2] == "float") or "float" in self.operation_types:
                LLVMGenerator.withdraw_last("int")
                LLVMGenerator.convert_to_float()
            else:
                LLVMGenerator.withdraw_last("int")
        elif v1_type == "float":
            LLVMGenerator.declare_assign_float(v1)
            LLVMGenerator.withdraw_last("float")
        values.append("%"+str(LLVMGenerator.reg-1))

        if "str" in self.operation_types:
            self.error(ctx.start.line, "Cannot perform arithmetic operations on strings. ")

        if "float" in self.operation_types:
            if ctx.op.text is "*":
                LLVMGenerator.mult_float(values[0], values[1])
            elif ctx.op.text is "/":
                LLVMGenerator.div_float(values[1], values[0])
            elif ctx.op.text is "+":
                LLVMGenerator.add_float(values[0], values[1])
            elif ctx.op.text is "-":
                LLVMGenerator.sub_float(values[1], values[0])
            self.operation_types.append("float")
            self.stack.append("float")
        else:
            if ctx.op.text is "*":
                LLVMGenerator.mult_i32(values[0], values[1])
            elif ctx.op.text is "/":
                LLVMGenerator.div_i32(values[1], values[0])
            elif ctx.op.text is "+":
                LLVMGenerator.add_i32(values[0], values[1])
            elif ctx.op.text is "-":
                LLVMGenerator.sub_i32(values[1], values[0])
            self.operation_types.append("int")
            self.stack.append("int")

        self.stack.append("%" + str(LLVMGenerator.reg-1))
        # print(self.stack[-1])

    def exitNumberExpr(self, ctx:LangParser.NumberExprContext):
        if ctx.value().number() is not None:
            if ctx.value().number().INT() is not None:
                self.stack.append("int")
                self.stack.append(int(ctx.value().number().INT().getText()))
                self.operation_types.append("int")
            if ctx.value().number().REAL() is not None:
                self.stack.append("float")
                self.stack.append(float(ctx.value().number().REAL().getText()))
                self.operation_types.append("float")
        if ctx.value().ID() is not None:
            id = ctx.value().ID().getText()
            if id not in self.variables.keys():
                self.error(ctx.start.line, "Variable has not been declared: " + id)
            self.stack.append("ID")
            self.stack.append(id)
            self.operation_types.append(self.variables[id])
        if ctx.value().STRING() is not None:
            self.stack.append("str")
            self.stack.append(ctx.value().STRING().getText()[1:-1])
            self.operation_types.append("string")

    def exitAssign(self, ctx:LangParser.AssignContext):
        id = ctx.ID().getText()
        v = self.stack.pop()
        v_type = self.stack.pop()

        if id in self.variables.keys() and self.variables[id] != v_type:
            if v_type == "ID":
                if self.variables[id] != self.variables[v]:
                    self.error(ctx.start.line, "Redefinition of type of variable " + id)
            else:
                self.error(ctx.start.line, "Redefinition of type of variable " + id)
        if "float" in self.operation_types:
            if id not in self.variables.keys():
                self.variables[id] = "float"
                LLVMGenerator.declare_float(id)
            if v_type == "ID":
                LLVMGenerator.withdraw_id(v, "float")
                LLVMGenerator.assign_float(id, "%" + str(LLVMGenerator.reg - 1))
            else:
                LLVMGenerator.assign_float(id, v)

        elif "int" in self.operation_types:
            if id not in self.variables.keys():
                self.variables[id] = "int"
                LLVMGenerator.declare_i32(id)
            if v_type == "ID":
                LLVMGenerator.withdraw_id(v, "int")
                LLVMGenerator.assign_i32(id, "%" + str(LLVMGenerator.reg - 1))
            else:
                LLVMGenerator.assign_i32(id, v)
        else:
            if id not in self.variables.keys():
                self.variables[id] = "str"
                LLVMGenerator.declare_string(id)
            if v_type == "ID":
                LLVMGenerator.withdraw_id(v, "str")
                LLVMGenerator.assign_string(id, "%" + str(LLVMGenerator.reg - 1))
            else:
                LLVMGenerator.assign_string(id, v)
        self.operation_types = []

    def enterIfExpr(self, ctx:LangParser.IfExprContext):
        left = "%" + str(LLVMGenerator.reg)
        right = "%" + str(LLVMGenerator.reg + 1)
        left_type = None
        right_type = None
        if ctx.left.number() is not None:
            if ctx.left.number().INT() is not None:
                left_type = "int"
                LLVMGenerator.declare_assign_i32(ctx.left.number().INT().getText())
            elif ctx.left.number().REAL() is not None:
                left_type = "float"
                LLVMGenerator.declare_assign_float(ctx.left.number().REAL().getText())
            left = "%" + str(LLVMGenerator.reg)
            LLVMGenerator.withdraw_last(left_type)
        elif ctx.left.ID() is not None:
            id = ctx.left.ID().getText()
            if id not in self.variables.keys():
                self.error(ctx.start.line, "Variable has not been declared: " + id)
            left_type = self.variables[id]
            LLVMGenerator.withdraw_id(id, self.variables[id])
        elif ctx.right.STRING() is not None:
            self.error("String comparison not allowed")

        if ctx.right.number() is not None:
            if ctx.right.number().INT() is not None:
                right_type = "int"
                LLVMGenerator.declare_assign_i32(ctx.right.number().INT().getText())
            elif ctx.right.number().REAL() is not None:
                right_type = "float"
                LLVMGenerator.declare_assign_float(ctx.right.number().REAL().getText())
            right = "%" + str(LLVMGenerator.reg)
            LLVMGenerator.withdraw_last(right_type)
        elif ctx.right.ID() is not None:
            id = ctx.right.ID().getText()
            if id not in self.variables.keys():
                self.error(ctx.start.line, "Variable has not been declared: " + id)
            right_type = self.variables[id]
            LLVMGenerator.withdraw_id(id, self.variables[id])
        elif ctx.right.STRING() is not None:
            self.error("String comparison not allowed")

        sgn = ctx.comp().getText()
        if left_type == "int" and right_type == "int":
            LLVMGenerator.compare_int(left, right, sgn)
        elif left_type == "float" and right_type == "float":
            LLVMGenerator.compare_float(left, right, sgn)
        elif left_type == "float" and right_type == "int":
            LLVMGenerator.convert_val_to_float(right)
            right = "%" + str(LLVMGenerator.reg - 1)
            LLVMGenerator.compare_float(left, right, sgn)
        elif left_type == "int" and right_type == "float":
            LLVMGenerator.convert_val_to_float(left)
            left = "%" + str(LLVMGenerator.reg - 1)
            LLVMGenerator.compare_float(left, right, sgn)
        
        res = "%" + str(LLVMGenerator.reg - 1)
        LLVMGenerator.begin_br(res)


    def exitIfExpr(self, ctx:LangParser.IfExprContext):
        LLVMGenerator.end_br() # TODO

    def exitProg(self, ctx:LangParser.ProgContext):
        with open("output.ll", "w") as f:
            f.write(LLVMGenerator.generate())
        print(">>>LLVM code generated to file output.ll<<<")
        # print(LLVMGenerator.generate())
