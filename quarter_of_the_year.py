import math

def quarter_of(month):
    return math.ceil(month / 12 * 4)

# other solutions

# explicit solutions
def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
    
# solution using importing ONLY ceil
from math import ceil
def quarter_of(month):
    return ceil(month / 3)

# integer division solution
def quarter_of(month):
    return (month + 2) // 3
