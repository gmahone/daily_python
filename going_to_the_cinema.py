def movie(card, ticket, perc):
    i = 1
    while True:
        card += (ticket * (perc**i))
        print(round(card))
        if round(card) < (ticket*i):
            return i
        i += 1
