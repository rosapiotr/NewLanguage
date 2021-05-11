declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@.stri = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.strd = private unnamed_addr constant [4 x i8] c"%f\0A\00", align 1
@.strlf = private unnamed_addr constant [4 x i8] c"%lf\00", align 1
@.strs = private unnamed_addr constant [4 x i8] c"%s\0A\00", align 1
@.strsf = private unnamed_addr constant [3 x i8] c"%s\00", align 1
@.strsfn = private unnamed_addr constant [6 x i8] c"%[^\0A]\00", align 1
@.str.1 = private unnamed_addr constant [5 x i8] c"test\00", align 1
@.str.2 = private unnamed_addr constant [6 x i8] c"test2\00", align 1

define void @test() #0 {
%a = alloca i8*, align 8
store i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.1, i32 0, i32 0), i8** %a, align 8
%1 = load i8*, i8** %a, align 8
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.strs, i32 0, i32 0), i8* %1)
%b = alloca i8*, align 8
store i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.2, i32 0, i32 0), i8** %b, align 8
ret void 
}

define i32 @main() #0{
%a = alloca i32
store i32 1, i32* %a
call void @test()
%1 = load i32, i32* %a
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.stri, i32 0, i32 0), i32 %1)
ret i32 0 }
