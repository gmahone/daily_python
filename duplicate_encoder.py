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


# other solutions

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

def duplicate_encode(word):
    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("
    return result


def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(x) == 1 else ')' for x in word)

def duplicate_encode(word):
    new_string = ""
    word = word.lower()
    
    for char in word:
        new_string += (")" if (word.count(char) > 1) else "(")
            
    return new_string
