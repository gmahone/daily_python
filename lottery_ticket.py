def bingo(ticket,win):
    mini_wins = 0
    for i in ticket:
        for j in i[0]:
            if ord(j) == i[1]:
                mini_wins += 1
                break
    return "Winner!" if mini_wins >= win else "Loser!"
