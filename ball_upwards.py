def calc_height(v, t):
    return (v * t) - (0.5 * 9.81 * t * t)
    

def max_ball(v0):
    v0 = v0 * 1000 / 3600
    height = 0
    time = 0.0
    while True:
        time += 0.1
        curr_height = calc_height(v0, time)
        print(curr_height)
        if curr_height > height:
            height = curr_height
        else:
            return round((time-0.1)*10)
