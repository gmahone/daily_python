def calc_height(v, t):
    return v * t - 0.5 * 9.81 * t * t
    

def max_ball(v0):
    v0 = v0 * 1000 / 60 * 60
    print(v0)
    height = 0
    time = 0
    while True:
        curr_height = calc_height(v0, time)
        time += 0.1
        if curr_height > height:
            height = curr_height
        else:
            return height
