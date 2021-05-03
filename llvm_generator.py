class LLVMGenerator:
    header_text = ""
    main_text = [""]
    reg = 1
    constants = 1
    constant_type = dict()
    depth = 0
    last_depth = 0

    def __init__(self):
        pass
    
    def declare_i32(id):
        LLVMGenerator.main_text[-1] += "%" + id + " = alloca i32\n"

    def declare_assign_i32(v):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = alloca i32\n"
        LLVMGenerator.main_text[-1] += "store i32 " + str(v) + ", i32* %" + str(LLVMGenerator.reg) +"\n"
        LLVMGenerator.reg += 1
        
    def declare_float(id):
        LLVMGenerator.main_text[-1] += "%" + id + " = alloca double\n"

    def declare_assign_float(v):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = alloca double\n"
        LLVMGenerator.main_text[-1] += "store double " + str(v) + ", double* %" + str(LLVMGenerator.reg) + "\n"
        LLVMGenerator.reg += 1

    def declare_string(id):
        LLVMGenerator.main_text[-1] += "%" + id + " = alloca i8*, align 8\n"

    def declare_assign_string(v):
        LLVMGenerator.header_text += "@.str." + str(LLVMGenerator.constants) + " = private unnamed_addr constant [" + str(len(v) + 1) + " x i8] c\"" + v + "\\00\", align 1\n"
        LLVMGenerator.constants += 1
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = alloca i8*, align 8\n"
        LLVMGenerator.main_text[-1] += "store i8* getelementptr inbounds ([" + str(len(v) + 1) + " x i8], [" + str(len(v) + 1) + " x i8]* @.str." + str(LLVMGenerator.constants - 1) + ", i32 0, i32 0), i8** %" + str(LLVMGenerator.reg) + ", align 8\n"
        LLVMGenerator.reg += 1

    def assign_i32(id, value):
        LLVMGenerator.main_text[-1] += "store i32 " + str(value) + ", i32* %" + id +"\n"

    # def assign_i32_number(value):
    #     LLVMGenerator.main_text[-1] += "store i32 " + str(value) + ", i32* %" + str(LLVMGenerator.reg) +"\n"

    def assign_float(id, value):
        LLVMGenerator.main_text[-1] += "store double " + str(value) + ", double* %" + id + "\n"

    # def assign_float_number(value):
    #     LLVMGenerator.main_text[-1] += "store double " + str(value) + ", double* %" + str(LLVMGenerator.reg) + "\n"

    def assign_string(id, value):
        # nie działa dla a = b
        LLVMGenerator.header_text += "@.str." + str(LLVMGenerator.constants) + " = private unnamed_addr constant [" + str(len(value) + 1) + " x i8] c\"" + value + "\\00\", align 1\n"
        LLVMGenerator.main_text[-1] += "store i8* getelementptr inbounds ([" + str(len(value) + 1) + " x i8], [" + str(len(value) + 1) + " x i8]* @.str." + str(LLVMGenerator.constants) + ", i32 0, i32 0), i8** %" + id + ", align 8\n"
        LLVMGenerator.constants += 1

    def add_i32(val1, val2):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = add nsw i32 " + val1 + ", " + val2 + "\n";
        LLVMGenerator.reg += 1

    def sub_i32(val1, val2):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = sub nsw i32 " + val1 + ", " + val2 + "\n";
        LLVMGenerator.reg += 1

    def mult_i32(val1, val2):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = mul nsw i32 " + val1 + ", " + val2 + "\n";
        LLVMGenerator.reg += 1
    
    def div_i32(val1, val2):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = sdiv i32 " + val1 + ", " + val2 + "\n";
        LLVMGenerator.reg += 1

    def add_float(val1, val2):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = fadd double " + val1 + ", " + val2 + "\n"
        LLVMGenerator.reg += 1

    def sub_float(val1, val2):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = fsub double " + val1 + ", " + val2 + "\n"
        LLVMGenerator.reg += 1

    def mult_float(val1, val2):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = fmul double " + val1 + ", " + val2 + "\n"
        LLVMGenerator.reg += 1

    def div_float(val1, val2):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = fdiv double " + val1 + ", " + val2 + "\n"
        LLVMGenerator.reg += 1

    def print_value(val):
        if isinstance(val, int):
            # LLVMGenerator.main_text[-1] += "%"+ LLVMGenerator.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i32 0, i32 0), i32 %"+ (LLVMGenerator.reg-1)+")\n";
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.stri, i32 0, i32 0), i32 "+ str(val) +")\n";
            LLVMGenerator.reg += 1
        elif isinstance(val, float):
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strd, i32 0, i32 0), double "+ str(val) +"00000e+00)\n";
            LLVMGenerator.reg += 1
        elif isinstance(val, str):
            # TODO
            pass
 
    def print_id(id, typ):
        if typ == "int":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = load i32, i32* %" + id + "\n"
            LLVMGenerator.reg += 1
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.stri, i32 0, i32 0), i32 %" + str(LLVMGenerator.reg-1) + ")\n"
            LLVMGenerator.reg += 1
        elif typ == "float":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = load double, double* %" + id + "\n"
            LLVMGenerator.reg += 1
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strd, i32 0, i32 0), double %" + str(LLVMGenerator.reg-1) + ")\n"
            LLVMGenerator.reg += 1
        elif typ == "str":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = load i8*, i8** %" + id + ", align 8\n"
            LLVMGenerator.reg += 1
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %" + str(LLVMGenerator.reg-1) + ")\n"
            LLVMGenerator.reg += 1
        elif typ == "strs":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = getelementptr inbounds [20 x i8], [20 x i8]* %" + id + ", i32 0, i32 0\n"
            LLVMGenerator.reg += 1
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %" + str(LLVMGenerator.reg-1) + ")\n"
            LLVMGenerator.reg += 1
    
    def withdraw_last(typ):
        if typ == "int":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = load i32, i32* %" + str(LLVMGenerator.reg-1) + "\n"
            LLVMGenerator.reg += 1
        if typ == "float":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = load double, double* %" + str(LLVMGenerator.reg-1) + "\n"
            LLVMGenerator.reg += 1

    def withdraw_id(id, typ):
        if typ == "int":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = load i32, i32* %" + id + "\n"
            LLVMGenerator.reg += 1
        elif typ == "float":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = load double, double* %" + id + "\n"
            LLVMGenerator.reg += 1
        elif typ == "str":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = load i8*, i8** %1, align 8\n"
            LLVMGenerator.reg += 1

    def convert_to_float():
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = sitofp i32 %" + str(LLVMGenerator.reg-1) + " to double\n"
        LLVMGenerator.reg += 1

    def convert_val_to_float(val):
        LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = sitofp i32 "+ val + " to double\n"
        LLVMGenerator.reg += 1

    def read_value(id, typ):
        if typ == 'int':
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.stri, i32 0, i32 0), i32* %" + id + ")\n"
            LLVMGenerator.reg += 1
        elif typ == 'float':
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strlf, i32 0, i32 0), double* %" + id + ")\n"
            LLVMGenerator.reg += 1
        elif typ == 'strs':
            LLVMGenerator.main_text[-1] += "%" + id + " = alloca [20 x i8], align 16\n"
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.strsfn, i32 0, i32 0), [20 x i8]* %" + id + ")\n"
            LLVMGenerator.reg += 1
        #declare + scanf
        pass

    def compare_int(left, right, sgn):
        if sgn == ">":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = icmp sgt i32 " + left + ", " + right + "\n"
            LLVMGenerator.reg += 1
        elif sgn == "<":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = icmp slt i32 " + left + ", " + right + "\n"
            LLVMGenerator.reg += 1
        elif sgn == "==":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = icmp eq i32 " + left + ", " + right + "\n"
            LLVMGenerator.reg += 1
        elif sgn == ">=":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = icmp sge i32 " + left + ", " + right + "\n"
            LLVMGenerator.reg += 1
        elif sgn == "<=":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = icmp sle i32 " + left + ", " + right + "\n"
            LLVMGenerator.reg += 1

    def compare_float(left, right, sgn):
        if sgn == ">":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = fcmp ogt double " + left + ", " + right + "\n"
            LLVMGenerator.reg += 1
        elif sgn == "<":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = fcmp olt double " + left + ", " + right + "\n"
            LLVMGenerator.reg += 1
        elif sgn == "==":
            LLVMGenerator.main_text[-1] += "%" + str(LLVMGenerator.reg) + " = fcmp eq double " + left + ", " + right + "\n"
            LLVMGenerator.reg += 1

    def begin_br(result):
        LLVMGenerator.main_text[-1] += "br i1 " + result + ", label %" + str(LLVMGenerator.reg) + ", " 
        LLVMGenerator.main_text.append("")
        LLVMGenerator.main_text[-1] += "; <label>:" + str(LLVMGenerator.reg) + ":\n"
        LLVMGenerator.reg += 1
        LLVMGenerator.depth += 1

    def end_br():
        LLVMGenerator.depth -= 1
        LLVMGenerator.main_text[LLVMGenerator.depth] += "label %" + str(LLVMGenerator.reg) + "\n"
        LLVMGenerator.main_text[-1] += "br label %" + str(LLVMGenerator.reg) + "\n"
        LLVMGenerator.main_text[-1] += "; <label>:" + str(LLVMGenerator.reg) + ":\n"
        LLVMGenerator.reg += 1
        if LLVMGenerator.depth == LLVMGenerator.last_depth:
            LLVMGenerator.last_depth = len(LLVMGenerator.main_text) - 1
            LLVMGenerator.depth = len(LLVMGenerator.main_text) - 1

    def generate():
        text = "";
        text += "declare i32 @printf(i8*, ...)\n";
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n";
        text += "@.stri = private unnamed_addr constant [4 x i8] c\"%d\\0A\\00\", align 1\n"
        text += "@.strd = private unnamed_addr constant [4 x i8] c\"%f\\0A\\00\", align 1\n"
        text += "@.strlf = private unnamed_addr constant [4 x i8] c\"%lf\\00\", align 1\n"
        text += "@.strs = private unnamed_addr constant [4 x i8] c\"%s\\0A\\00\", align 1\n"
        text += "@.strsf = private unnamed_addr constant [3 x i8] c\"%s\\00\", align 1\n"
        text += "@.strsfn = private unnamed_addr constant [6 x i8] c\"%[^\\0A]\\00\", align 1\n"
        text += LLVMGenerator.header_text;
        text += "define i32 @main() #0{\n";
        for mt in LLVMGenerator.main_text:
            text += mt;
        text += "ret i32 0 }\n";

        # i = 1
        # for mt in LLVMGenerator.main_text:
        #     print(str(i) + " - " + mt)
        #     i += 1

        return text;