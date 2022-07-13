# find k unique values of a list ls
#  that sum up to a value as closely as possible
#  to a given value t (inclusive), but do not go over it

# need to produce all possible combinations of k values

# example code for itertools
#import itertools
#
#stuff = [1, 2, 3]
#for L in range(0, len(stuff)+1):
#    for subset in itertools.combinations(stuff, L):
#        print(subset)
## end example

import itertools

def choose_best_sum(t, k, ls):
    best_set = [t]
    for subset in itertools.combinations(ls, k):
        if 0 <= (t - sum(subset)) < sum(best_set):
            best_set = subset
    return None if best_set == t else sum(best_set)
