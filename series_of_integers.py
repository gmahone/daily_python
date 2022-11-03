def generate_integers(m, n): 
    return [i for i in range(m,n+1)]

# using only range
def generate_integers(m, n): 
    return list(range(m,n+1))

# similar range solution
def generate_integers(m, n): 
    return [*range(m, n + 1)]
