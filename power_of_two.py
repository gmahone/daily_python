def power_of_two(x):
  curr_power = 0
  while 2**curr_power < x:
    curr_power += 1
  return True if 2**curr_power == x else False


# math solution
def power_of_two(x):
    return x != 0 and ((x & (x - 1)) == 0)
