
# This is just a simple test CLI Calculator


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Choose operator: +, -, /, *, % ")

if op == "+":
    result = num1 + num2
    
elif op =="-":
    result = num1 - num2
    
elif op =="*":
    result = num1 * num2
    
elif op =="/":
    result = num1 / num2
    
elif op =="%":
    result = num1 % num2
    
else:
    print("Enter valid operator")
    
result = print("The result is of {} {} {} = ".format(num1, op, num2), result)

   