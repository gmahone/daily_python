def problem(a):
    try:
        return 50 * a + 6
    except TypeError:
        return "Error"

# other solutions

# other formulation, using isinstance
def problem(a):
    return "Error" if isinstance(a,str) else a*50+6
