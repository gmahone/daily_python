def str_count(strng, letter):
    return list(strng).count(letter)

# don't need to create a list first
def strCount(string, letter):
    return string.count(letter)


# looping solution for laughs
def str_count(strng, letter):
    result = 0
    for chr in strng:
        if chr == letter:
            result += 1
    return result
