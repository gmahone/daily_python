def to_nato(words):
    words = "".join(words.split(" "))
    " ".join(NATO.get(x, x) for x in words)
    pass
