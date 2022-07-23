def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0


# alternative solution
def is_divisible(wall_length, pixel_size):
    return not wall_length % pixel_size
