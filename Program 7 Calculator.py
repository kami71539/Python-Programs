num1=float(input("Enter first number: "))
op=input("What would you like to do to them ?")
num2=float(input("Enter second number: "))
if (op =='+'):
    print(num1, '+' ,num2,"is",num1+num2)
elif (op=='-'):
    print(num1, '-' ,num2,"is",num1-num2)
elif(op=='*'):
    print(num1, '*' ,num2,"is",num1*num2)
elif(op=='/'):
    print(num1, '/' ,num2,"is",num1/num2)
elif(op=='%'):
    print(num1, '%' ,num2,"is",num1%num2)
else:
    print("Don't be ridicuous")
    
print(num1, '+' ,num2,"is",num1+num2)
print(num1, '-' ,num2,"is",num1-num2)
print(num1, '*' ,num2,"is",num1*num2)
print(num1, '/' ,num2,"is",num1/num2)
print(num1, '%' ,num2,"is",num1%num2)