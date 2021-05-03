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
@.str.3 = private unnamed_addr constant [17 x i8] c"a mniejsze od 10\00", align 1
@.str.4 = private unnamed_addr constant [2 x i8] c"A\00", align 1
@.str.5 = private unnamed_addr constant [2 x i8] c"B\00", align 1
@.str.6 = private unnamed_addr constant [2 x i8] c"C\00", align 1
@.str.7 = private unnamed_addr constant [2 x i8] c"D\00", align 1
@.str.8 = private unnamed_addr constant [9 x i8] c"IT WORKS\00", align 1
@.str.9 = private unnamed_addr constant [6 x i8] c"FALSE\00", align 1
@.str.10 = private unnamed_addr constant [5 x i8] c"TRUE\00", align 1
define i32 @main() #0{
%a = alloca i32
store i32 7, i32* %a
%1 = load i32, i32* %a
%2 = alloca i32
store i32 2, i32* %2
%3 = load i32, i32* %2
%4 = icmp sgt i32 %1, %3
br i1 %4, label %5, label %27
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
%18 = load i32, i32* %a
%19 = alloca i32
store i32 10, i32* %19
%20 = load i32, i32* %19
%21 = icmp slt i32 %18, %20
br i1 %21, label %22, label %26
; <label>:22:
%23 = alloca i8*, align 8
store i8* getelementptr inbounds ([17 x i8], [17 x i8]* @.str.3, i32 0, i32 0), i8** %23, align 8
%24 = load i8*, i8** %23, align 8
%25 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %24)
br label %26
; <label>:26:
br label %27
; <label>:27:
store i32 12, i32* %a
%28 = load i32, i32* %a
%29 = alloca i32
store i32 12, i32* %29
%30 = load i32, i32* %29
%31 = icmp sgt i32 %28, %30
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
store i32 12, i32* %38
%39 = load i32, i32* %38
%40 = icmp sge i32 %37, %39
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
%49 = icmp slt i32 %46, %48
br i1 %49, label %50, label %54
; <label>:50:
%51 = alloca i8*, align 8
store i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.6, i32 0, i32 0), i8** %51, align 8
%52 = load i8*, i8** %51, align 8
%53 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %52)
br label %54
; <label>:54:
%55 = load i32, i32* %a
%56 = alloca i32
store i32 10, i32* %56
%57 = load i32, i32* %56
%58 = icmp sgt i32 %55, %57
br i1 %58, label %59, label %63
; <label>:59:
%60 = alloca i8*, align 8
store i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.7, i32 0, i32 0), i8** %60, align 8
%61 = load i8*, i8** %60, align 8
%62 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %61)
br label %63
; <label>:63:
store i32 1, i32* %a
%64 = load i32, i32* %a
%65 = alloca double
store double 2.1, double* %65
%66 = load double, double* %65
%67 = sitofp i32 %64 to double
%68 = fcmp olt double %67, %66
br i1 %68, label %69, label %73
; <label>:69:
%70 = alloca i8*, align 8
store i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.8, i32 0, i32 0), i8** %70, align 8
%71 = load i8*, i8** %70, align 8
%72 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %71)
br label %73
; <label>:73:
%74 = alloca i32
store i32 5, i32* %74
%75 = load i32, i32* %74
%76 = alloca double
store double 5.1, double* %76
%77 = load double, double* %76
%78 = sitofp i32 %75 to double
%79 = fcmp ogt double %78, %77
br i1 %79, label %80, label %84
; <label>:80:
%81 = alloca i8*, align 8
store i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.9, i32 0, i32 0), i8** %81, align 8
%82 = load i8*, i8** %81, align 8
%83 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %82)
br label %84
; <label>:84:
%85 = alloca i32
store i32 5, i32* %85
%86 = load i32, i32* %85
%87 = alloca double
store double 5.1, double* %87
%88 = load double, double* %87
%89 = sitofp i32 %86 to double
%90 = fcmp olt double %89, %88
br i1 %90, label %91, label %95
; <label>:91:
%92 = alloca i8*, align 8
store i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.10, i32 0, i32 0), i8** %92, align 8
%93 = load i8*, i8** %92, align 8
%94 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %93)
br label %95
; <label>:95:
ret i32 0 }
