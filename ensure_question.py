def ensure_question(s):
    #print(s[-1:])
    return s if s[-1:] == "?" else "{}?".format(s)
