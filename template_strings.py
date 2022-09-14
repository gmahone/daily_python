def temple_strings(obj, feature): 
    return f"{obj} are {feature}"

## alternative with .format
def temple_strings(obj, feature): 
    return "{} are {}".format(obj, feature)
