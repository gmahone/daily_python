def to_nato(words):
    words = "".join(words.split(" "))
    result = " ".join(NATO.get(x.upper(), x) for x in words)
    return result

# single line
def to_nato(words):
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')
