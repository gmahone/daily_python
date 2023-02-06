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

    
# using a dict and lambda functions
def calculate(num1, operation, num2):
    ops = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y), "*": (lambda x, y: x * y), "/": (lambda x, y: x / y)}
    try: return ops[operation](num1, num2)
    except: return None
