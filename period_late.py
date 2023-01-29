def period_is_late(last,today,cycle_length):
    lag = today - last
    return lag.days > cycle_length
