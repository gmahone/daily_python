def cube_checker(volume, side):
    return True if side**3 == abs(volume) and volume != 0 else False
