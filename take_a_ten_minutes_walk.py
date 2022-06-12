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
        
# other solutions

# testing the counts of each pair
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# another paired count solution
def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False
