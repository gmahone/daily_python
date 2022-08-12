def cube_checker(volume, side):
    return True if side**3 == abs(volume) and volume != 0 and volume > 0 else False


## simpler formulation
def cube_checker(volume, side):
    return 0 < volume == side**3

# another formulation
def cube_checker(volume, side):
    return side > 0 and side ** 3 == volume
