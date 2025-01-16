num1 = int(input("Enter the value of 1st num:"))
num2 = int(input("Enter the value of 2nd num:"))
operator = input("Enter the operator to perform the operation")
if(operator == "+"):
    print("Addition of num1 and num2 is = ", num1 + num2)

elif(operator == "-"):
    print("Substraction of num1 and num2 is = ", num1 - num2)

elif(operator == "*"):
    print("Multiplication of num1 and num2 is = ", num1 * num2)

elif(operator == "/"):
    print("Divisionn of num1 and num2 is = ", num1 / num2)

else:
    print("Invalid operation. Please enter numerical valus.")

