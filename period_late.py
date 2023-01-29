def period_is_late(last,today,cycle_length):
    lag = today - last
    return lag.days > cycle_length

# shorter solution
def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length
