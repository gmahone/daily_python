def remove(s, n):
    return s.replace("!", "", n)

# as a lambda
remove=lambda s,n:s.replace('!','',n)

# using split rather than replace
def remove(s, n):
    return ''.join(s.split('!', n))
