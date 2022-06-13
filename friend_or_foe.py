def friend_finder(item):
    if len(item) == 4:
        return True
    else:
        return False

def friend(x):
    result = list(filter(friend_finder, x))
    return result
