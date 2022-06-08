def hoop_count(n):
    result = "Great, now move on to tricks"
    if n < 10:
        result = "Keep at it until you get it"
    return result

# ternary
def hoop_count(n):
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"

# reverse ternary
def hoopCount(n):
    return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"


# if else function
def hoopCount(n):
    if n >= 10:
        return 'Great, now move on to tricks'
    else:
        return 'Keep at it until you get it'
