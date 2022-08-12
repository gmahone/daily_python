def isDigit(string):
    try:
        float(string)
    except:
        return False
    return True

# alternative layout
def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False
