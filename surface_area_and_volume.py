def get_size(w,h,d):
    volume = w * h * d
    surface_area = (2 * w * h) + (2 * w * d) + (2 * h * d)
    return [surface_area, volume]

# lambda version
get_size = lambda w,h,d: [(2 * w * h) + (2 * w * d) + (2 * h * d), w * h * d]
