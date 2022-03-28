def count(string):
    counts = dict()
    for i in string:
        counts[i] = counts.get(i,0) + 1
    return counts

# add other solutions

def count(string):
    return {i: string.count(i) for i in string}

def count(s):
    return {x:s.count(x) for x in set(s)}
