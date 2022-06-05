def powers_of_two(n):
    result = [];
    for i in range(0, n+1):
        result.append(2**i)
    return result
        
# other solutions

# simpler version
def powers_of_two(n):
    return [2**x for x in range(n+1)]
