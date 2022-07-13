def derive(coefficient, exponent): 
    return f"{coefficient*exponent}x^{exponent-1}" if exponent > 2 else f"{coefficient*exponent}x"

# solution using format
def derive(coefficient, exponent): 
    return("{}x^{}".format(coefficient*exponent, exponent-1))
