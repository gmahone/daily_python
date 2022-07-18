def power_of_two(x):
  power = 0
  while 2**power < x:
    power += 1
  return True if 2**power == x else False
