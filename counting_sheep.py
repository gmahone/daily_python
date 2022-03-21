def true_counter(arr):
    true_vals = 0
    for i in range(0, len(arr)):
        if arr[i]:
            true_vals += 1
    return true_vals



test_arr = [True, True, False, True, False, True]

print(true_counter(test_arr))


# other solutions
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)


def count_sheeps(array_of_sheep):
  # TODO May the force be with you
  count = 0
  for sheep in array_of_sheep:
      if sheep:
          count += 1 
  return count
