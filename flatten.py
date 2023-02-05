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
