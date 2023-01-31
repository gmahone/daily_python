def bingo(ticket,win):
    mini_wins = 0
    for i in ticket:
        for j in i[0]:
            if ord(j) == i[1]:
                mini_wins += 1
                break
    return "Winner!" if mini_wins >= win else "Loser!"


# single line
def bingo(ticket, win):
    return 'Winner!' if sum(chr(n) in s for s, n in ticket) >= win else 'Loser!'
