num1= int(input("Enter the first number"))
num2=int(input("Enter the second number"))

operation= input("Enter the operation (+,-, *,/):")
if operation == "+":
  print("the sum is",num1 + num2)
elif operation == "-":
  print("the difference is", num1-num2)
elif operation == "*":
  print("the pruduct is", num1*num2)
elif operation== "/":
  if num2 != 0:
    print("the quotient is", num1/num2)
  else:
    print("Error: Division by zero is not allowed.")
else:
  print("Invalid operation entered.")