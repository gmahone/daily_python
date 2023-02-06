def calculate(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        try:
            result = num1 / num2
        except:
            result = None
    else:
        result = None
    print(result)
    pass
