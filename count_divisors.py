def divisors(n):
    out = []
    for i in range(1, n+1):
        if n % i == 0:
            out.append(i)
    return len(out)
  
# other solutions

# Time: 11724ms
def divisors5(n):
    return len(list(filter(lambda e: isinstance(e, int), [x if n % x == 0 else None for x in range(1, n + 1)])))

# Time: 7546ms
def divisors4(n):
    return len(list(filter(lambda e: e, [True if n % x == 0 else False for x in range(1, n + 1)])))

# Time: 4731ms
def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])

# Time: 3675ms
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])

divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])


def divisors(n):
    return sum(1 for i in xrange(1, n + 1) if n % i == 0)


def divisors(n):
    count=0
    for i in xrange(1,n/2+1):
        if n%i==0: count+=1
    return count+1
