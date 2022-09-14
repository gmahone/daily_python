def temple_strings(obj, feature): 
    return f"{obj} are {feature}"

## alternative with .format
def temple_strings(obj, feature): 
    return "{} are {}".format(obj, feature)

## alternative with direct string pasting
def temple_strings(obj, feature): 
    return obj + " are " + feature
