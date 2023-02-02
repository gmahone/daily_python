def to_nato(words):
    words = "".join(words.split(" "))
    result = " ".join(NATO.get(x.upper(), x) for x in words)
    print(result)
    pass
