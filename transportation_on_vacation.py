def rental_car_cost(d):
    result = 40 * d
    if d > 6:
        result -= 50
    elif d > 2:
        result -= 20
    return result

# other solutions

# solution using in line boolean conversion
def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30
