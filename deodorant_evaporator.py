def evaporator(content, evap_per_day, threshold):
    threshold = content * threshold/100
    i = 0
    while content > threshold:
        content -= content * evap_per_day/100
        i += 1
    return i
