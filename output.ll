declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@.stri = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.strd = private unnamed_addr constant [4 x i8] c"%f\0A\00", align 1
@.strlf = private unnamed_addr constant [4 x i8] c"%lf\00", align 1
@.strs = private unnamed_addr constant [4 x i8] c"%s\0A\00", align 1
@.strsf = private unnamed_addr constant [3 x i8] c"%s\00", align 1
@.strsfn = private unnamed_addr constant [6 x i8] c"%[^\0A]\00", align 1
@.str.1 = private unnamed_addr constant [9 x i8] c"testtest\00", align 1

define void @test(i8*, i32, double) #0 {
%a = alloca i8*, align 8
store i8* %0, i8** %a, align 8
%b = alloca i32
store i32 %1, i32* %b
%c = alloca double
store double %2, double* %c
%4 = load i8*, i8** %a, align 8
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %4)
%6 = load i32, i32* %b
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.stri, i32 0, i32 0), i32 %6)
%8 = load double, double* %c
%9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strd, i32 0, i32 0), double %8)
%10 = load double, double* %c
%11 = load i32, i32* %b
%12 = sitofp i32 %11 to double
%13 = fmul double %10, %12
%14 = alloca i32
store i32 1, i32* %14
%15 = load i32, i32* %14
%16 = sitofp i32 %15 to double
%17 = alloca double
store double %13, double* %17
%18 = load double, double* %17
%19 = fadd double %16, %18
%20 = alloca double
store double %19, double* %20
%21 = load double, double* %20
%22 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strd, i32 0, i32 0), double %21)
ret void 
}

define i32 @main() #0{
call void @test(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.1, i32 0, i32 0), i32 1, double 2.0)
ret i32 0 }
