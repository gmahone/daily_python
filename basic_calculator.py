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
    return result


# using eval
def calculate(num1, operation, num2): 
    try :
        return eval("{} {} {}".format(num1, operation, num2))
    except (ZeroDivisionError, SyntaxError):
        return None
