declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@.stri = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.strd = private unnamed_addr constant [4 x i8] c"%f\0A\00", align 1
@.strlf = private unnamed_addr constant [4 x i8] c"%lf\00", align 1
@.strs = private unnamed_addr constant [4 x i8] c"%s\0A\00", align 1
@.strsf = private unnamed_addr constant [3 x i8] c"%s\00", align 1
@.strsfn = private unnamed_addr constant [6 x i8] c"%[^\0A]\00", align 1
@.str.1 = private unnamed_addr constant [15 x i8] c"a wieksze od 2\00", align 1
@.str.2 = private unnamed_addr constant [15 x i8] c"a wieksze od 4\00", align 1
@.str.3 = private unnamed_addr constant [2 x i8] c"A\00", align 1
@.str.4 = private unnamed_addr constant [2 x i8] c"B\00", align 1
@.str.5 = private unnamed_addr constant [2 x i8] c"C\00", align 1
@.str.6 = private unnamed_addr constant [2 x i8] c"D\00", align 1
@.str.7 = private unnamed_addr constant [9 x i8] c"IT WORKS\00", align 1
@.str.8 = private unnamed_addr constant [6 x i8] c"FALSE\00", align 1
@.str.9 = private unnamed_addr constant [5 x i8] c"TRUE\00", align 1
define i32 @main() #0{
%a = alloca i32
store i32 7, i32* %a
%1 = load i32, i32* %a
%2 = alloca i32
store i32 2, i32* %2
%3 = load i32, i32* %2
%4 = icmp sgt i32 %1, %3
br i1 %4, label %5, label %18
; <label>:5:
%6 = alloca i8*, align 8
store i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.str.1, i32 0, i32 0), i8** %6, align 8
%7 = load i8*, i8** %6, align 8
%8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %7)
%9 = load i32, i32* %a
%10 = alloca i32
store i32 4, i32* %10
%11 = load i32, i32* %10
%12 = icmp sgt i32 %9, %11
br i1 %12, label %13, label %17
; <label>:13:
%14 = alloca i8*, align 8
store i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.str.2, i32 0, i32 0), i8** %14, align 8
%15 = load i8*, i8** %14, align 8
%16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %15)
br label %17
; <label>:17:
br label %18
; <label>:18:
store i32 12, i32* %a
%19 = load i32, i32* %a
%20 = alloca i32
store i32 12, i32* %20
%21 = load i32, i32* %20
%22 = icmp sgt i32 %19, %21
br i1 %22, label %23, label %27
; <label>:23:
%24 = alloca i8*, align 8
store i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.3, i32 0, i32 0), i8** %24, align 8
%25 = load i8*, i8** %24, align 8
%26 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %25)
br label %27
; <label>:27:
%28 = load i32, i32* %a
%29 = alloca i32
store i32 12, i32* %29
%30 = load i32, i32* %29
%31 = icmp sge i32 %28, %30
br i1 %31, label %32, label %36
; <label>:32:
%33 = alloca i8*, align 8
store i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.4, i32 0, i32 0), i8** %33, align 8
%34 = load i8*, i8** %33, align 8
%35 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %34)
br label %36
; <label>:36:
%37 = load i32, i32* %a
%38 = alloca i32
store i32 10, i32* %38
%39 = load i32, i32* %38
%40 = icmp slt i32 %37, %39
br i1 %40, label %41, label %45
; <label>:41:
%42 = alloca i8*, align 8
store i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.5, i32 0, i32 0), i8** %42, align 8
%43 = load i8*, i8** %42, align 8
%44 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %43)
br label %45
; <label>:45:
%46 = load i32, i32* %a
%47 = alloca i32
store i32 10, i32* %47
%48 = load i32, i32* %47
%49 = icmp sgt i32 %46, %48
br i1 %49, label %50, label %54
; <label>:50:
%51 = alloca i8*, align 8
store i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.6, i32 0, i32 0), i8** %51, align 8
%52 = load i8*, i8** %51, align 8
%53 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %52)
br label %54
; <label>:54:
store i32 1, i32* %a
%55 = load i32, i32* %a
%56 = alloca double
store double 2.1, double* %56
%57 = load double, double* %56
%58 = sitofp i32 %55 to double
%59 = fcmp olt double %58, %57
br i1 %59, label %60, label %64
; <label>:60:
%61 = alloca i8*, align 8
store i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.7, i32 0, i32 0), i8** %61, align 8
%62 = load i8*, i8** %61, align 8
%63 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %62)
br label %64
; <label>:64:
%65 = alloca i32
store i32 5, i32* %65
%66 = load i32, i32* %65
%67 = alloca double
store double 5.1, double* %67
%68 = load double, double* %67
%69 = sitofp i32 %66 to double
%70 = fcmp ogt double %69, %68
br i1 %70, label %71, label %75
; <label>:71:
%72 = alloca i8*, align 8
store i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.8, i32 0, i32 0), i8** %72, align 8
%73 = load i8*, i8** %72, align 8
%74 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %73)
br label %75
; <label>:75:
%76 = alloca i32
store i32 5, i32* %76
%77 = load i32, i32* %76
%78 = alloca double
store double 5.1, double* %78
%79 = load double, double* %78
%80 = sitofp i32 %77 to double
%81 = fcmp olt double %80, %79
br i1 %81, label %82, label %86
; <label>:82:
%83 = alloca i8*, align 8
store i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.9, i32 0, i32 0), i8** %83, align 8
%84 = load i8*, i8** %83, align 8
%85 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %84)
br label %86
; <label>:86:
ret i32 0 }
