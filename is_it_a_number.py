def isDigit(string):
    try:
        float(string)
    except:
        return False
    return True
