def filter_odd(x):
  return x % 2 != 0

odds = lambda a: list(filter(filter_odd, a))


## add solution using for in if
def odds(values):
        return [i for i in values if i%2]
