def friend_finder(item):
    return len(item) == 4

def friend(x):
    return filter(x, friend_finder)
