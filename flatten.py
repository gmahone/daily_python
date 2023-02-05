# fails random tests
def flatten(lst):
    try:
        result = [i for sublst in lst for i in sublst]
    except:
        result = lst
    return result

# another solution that fails random tests
import itertools

def flatten(lst):
    try:
        result = list(itertools.chain(*lst))
    except: 
        result = lst
    return result

# another solution
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result = result + i
        else:
            result.append(i)
    return result


# another solution
def flatten(lst):
    r = []
    for x in lst:
       if type(x) is list:
          r.extend(x)
       else:
          r.append(x)
    return r 
