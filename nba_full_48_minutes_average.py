def nba_extrap(ppg, mpg):
    return round(ppg/mpg*48,1) if mpg else 0
