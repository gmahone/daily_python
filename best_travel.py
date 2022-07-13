# find k unique values of a list ls
#  that sum up to a value as closely as possible
#  to a given value t (inclusive), but do not go over it

# need to produce all possible combinations of k values

# example code for itertools
import itertools

stuff = [1, 2, 3]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        print(subset)
## end example

def choose_best_sum(t, k, ls):
    pass
