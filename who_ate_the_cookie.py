def cookie(x):
    if type(x) is str:
        print("String")
    elif type(x) is int or type(x) is float:
        print("Number")
    else:
        print("Other")
    pass
