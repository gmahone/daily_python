def cookie(x):
    if type(x) is str:
        culprit = "Zach"
    elif type(x) is int or type(x) is float:
        culprit = "Monica"
    else:
        culprit = "the dog"
    return "Who ate the last cookie? It was {}!".format(culprit)


# using get type
def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")


## using try
def cookie(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who
