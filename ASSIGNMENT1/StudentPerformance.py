#student performance
d=int(input("Enter the marks of student:- "))
if d>=90 and d<=100:
    print("excellent marks")
elif d>=70 and d<=89:
    print(" Best marks")
elif d>=50 and d<=69:
    print("good marks")
elif d>=35 and d<=49:
    print("Avarge marks")
elif d>=0 and d<=34:
    print("The Student is Fail")
else:
    print("Enter the valid marks!!")
# Enter the students marks:- 30
# student is fail