def rental_car_cost(d):
    result = 40 * d
    if d > 6:
        result -= 50
    elif d > 2:
        result -= 20
    return result
