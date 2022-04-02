def count_chars(items):
    counts = dict()
    for i in items:
        counts[i] = counts.get(i, 0) + 1
    return counts

def duplicate_encode(word):
    word = word.upper()
    counts = count_chars(word)
    out = ""
    for i in range(0, len(word)):
        if counts[word[i]] > 1:
            out = out + ")"
        else:
            out = out + "("
    return out
