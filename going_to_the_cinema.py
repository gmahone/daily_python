def movie(card, ticket, perc):
    i = 1
    while True:
        card += (ticket * (perc**i))
        print(round(card))
        if i > 5:
            return "Stopped"
        i += 1
