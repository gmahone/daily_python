def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce >= 1 or bounce <= 0 or window >= h:
        return -1
    else:
        i = 1
        h *= bounce
        while h > window:
            i += 2
            h *= bounce
        return i

    
# other solutions

def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1

def bouncingBall(h, bounce, window):
    seen = -1
    
    if 0 < bounce < 1:
        while h > window > 0:
            seen += 2
            h *= bounce
    
    return seen

def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    return 2 + bouncingBall(h * bounce, bounce, window)

def bouncingBall(h, bounce, window):
    count = -1
    if bounce >= 1 or bounce < 0: return -1 
    while(h > window):
        count += 2
        h = h*bounce
    
    return count
