def evaporator(content, evap_per_day, threshold):
    threshold = content * threshold/100
    i = 0
    while content > threshold:
        content -= content * evap_per_day/100
        i += 1
    return i

# other solutions
import math
def evaporator(content, evap_per_day, threshold):
    return int(math.ceil(math.log(threshold/100.0, 1.0-evap_per_day/100.0)))
