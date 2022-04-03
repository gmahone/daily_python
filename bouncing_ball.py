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
