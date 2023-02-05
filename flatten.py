def flatten(lst):
    try:
        result = [i for sublst in lst for i in sublst]
    except:
        result = lst
    return result
