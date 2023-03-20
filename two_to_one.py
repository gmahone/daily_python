def longest(a1, a2):
    result = ""
    new = a1 + a2
    for i in new:
        if i not in result:
            result += i
    return "".join(sorted(result))

## solution using set
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

# add solution using set and union
def longest(s1, s2):
    return ''.join(sorted(set(s1).union(s2)))
