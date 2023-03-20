def longest(a1, a2):
    result = ""
    new = a1 + a2
    for i in new:
        if i not in result:
            result += i
    print(sorted(result))
    pass
