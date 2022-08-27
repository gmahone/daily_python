def filter_odd(x):
  return x % 2 != 0

odds = lambda a: list(filter(filter_odd, a))
