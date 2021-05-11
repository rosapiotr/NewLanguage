declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@.stri = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.strd = private unnamed_addr constant [4 x i8] c"%f\0A\00", align 1
@.strlf = private unnamed_addr constant [4 x i8] c"%lf\00", align 1
@.strs = private unnamed_addr constant [4 x i8] c"%s\0A\00", align 1
@.strsf = private unnamed_addr constant [3 x i8] c"%s\00", align 1
@.strsfn = private unnamed_addr constant [6 x i8] c"%[^\0A]\00", align 1
@.str.1 = private unnamed_addr constant [34 x i8] c"Comparison of INT and FLOAT works\00", align 1
@.str.2 = private unnamed_addr constant [43 x i8] c"Comparison of INT variable and FLOAT works\00", align 1
@.str.3 = private unnamed_addr constant [44 x i8] c"Comparison of INT and FLOAT variables works\00", align 1

define i32 @main() #0{
%1 = alloca i32
store i32 100, i32* %1
%2 = load i32, i32* %1
%3 = alloca double
store double 100.1, double* %3
%4 = load double, double* %3
%5 = sitofp i32 %2 to double
%6 = fcmp olt double %5, %4
br i1 %6, label %7, label %11

; <label>:7:
%8 = alloca i8*, align 8
store i8* getelementptr inbounds ([34 x i8], [34 x i8]* @.str.1, i32 0, i32 0), i8** %8, align 8
%9 = load i8*, i8** %8, align 8
%10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %9)
br label %11

; <label>:11:
%a = alloca i32
store i32 1, i32* %a
%12 = load i32, i32* %a
%13 = alloca double
store double 2.1, double* %13
%14 = load double, double* %13
%15 = sitofp i32 %12 to double
%16 = fcmp olt double %15, %14
br i1 %16, label %17, label %21

; <label>:17:
%18 = alloca i8*, align 8
store i8* getelementptr inbounds ([43 x i8], [43 x i8]* @.str.2, i32 0, i32 0), i8** %18, align 8
%19 = load i8*, i8** %18, align 8
%20 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %19)
br label %21

; <label>:21:
%b = alloca double
store double 1.1, double* %b
%22 = load i32, i32* %a
%23 = load double, double* %b
%24 = sitofp i32 %22 to double
%25 = fcmp olt double %24, %23
br i1 %25, label %26, label %30

; <label>:26:
%27 = alloca i8*, align 8
store i8* getelementptr inbounds ([44 x i8], [44 x i8]* @.str.3, i32 0, i32 0), i8** %27, align 8
%28 = load i8*, i8** %27, align 8
%29 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %28)
br label %30

; <label>:30:
ret i32 0 }
