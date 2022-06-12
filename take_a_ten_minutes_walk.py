def is_valid_walk(walk):
    dict_opposites = {"n": "s", "s": "n", "e": "w", "w": "e"}
    if len(walk) != 10 or len(walk) % 2:
        return False
    while True:
        currentLen = len(walk)
        if currentLen == 0:
            return True
        currentVal = walk.pop()
        if dict_opposites[currentVal] in walk:
            walk.remove(dict_opposites[currentVal])
        else:
            return False
