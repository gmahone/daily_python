def movie(card, ticket, perc):
    i <- 1
    while true:
        card += (ticket * (perc^i))
        print(round(card))
        if i > 5:
            return "Stopped"
