def position(alphabet):
    return f"Position of alphabet: {ord(alphabet) - 96}"

# same solution with format
def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)

# another format using index finding and sprintf like
def position(alphabet):
    return "Position of alphabet: %s" % ("abcdefghijklmnopqrstuvwxyz".find(alphabet) + 1)
