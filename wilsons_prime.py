def am_i_wilson(n):
    wilson_primes = [5,13,563]
    return n in wilson_primes


## alternative
def am_i_wilson(n):
    return n in (5, 13, 563)
