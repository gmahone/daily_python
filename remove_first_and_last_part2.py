def array(string):
    result = string.split(",")
    return None if len(result) < 3 else " ".join(result.slice(1,len(result)))
