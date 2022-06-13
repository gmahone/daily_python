def friend_finder(item):
    if len(item) == 4:
        return True
    else:
        return False

def friend(x):
    result = list(filter(friend_finder, x))
    return result


# other solutions

# solution not using filter
def friend(x):
    return [f for f in x if len(f) == 4]
