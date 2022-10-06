import math
def movie(card, ticket, perc):
    i = 1
    while True:
        card += (ticket * (perc**i))
        if math.ceil(card) < (ticket*i):
            return i
        i += 1
