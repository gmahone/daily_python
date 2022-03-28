def count(string):
    counts = dict()
    for i in string:
        counts[i] = counts.get(i,0) + 1
    return counts
