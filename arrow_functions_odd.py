def filter_odd(x):
  return x % 2 != 0

odds = lambda a: list(filter(filter_odd, a))


## add solution using for in if
def odds(values):
        return [i for i in values if i%2]

## lambda version
odds = lambda o: [i for i in o if i % 2 != 0]


## using lambda within function and bitwise operation
def odds(values):
    return list(filter(lambda x: x&1,values))
