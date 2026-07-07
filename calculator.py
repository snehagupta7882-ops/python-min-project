num1=int(input("enter the number"))
num2=int(input("enter the number"))
operator=input("enter the operator (+,-,*,/,%,**) ")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator=="%":
    print(num1%num2)
elif operator=="**":
    print(num1**num2)
else:
    print("error")