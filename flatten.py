def flatten(lst):
    result = []
    try:
        result = [i for sublst in lst for i in sublst]
    except:
        result = lst
    print(result)
    pass
