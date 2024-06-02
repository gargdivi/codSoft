def calculator():
    print("Welcome to the simple calculator!")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number corresponding to the operation: ")

    if operation == '1':
        result = num1 + num2
        operation_sign = '+'
    elif operation == '2':
        result = num1 - num2
        operation_sign = '-'
    elif operation == '3':
        result = num1 * num2
        operation_sign = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_sign = '/'
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice. Please select a valid operation.")
        return

    print(f"The result of {num1} {operation_sign} {num2} is: {result}")

calculator()
