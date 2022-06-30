def stairs_in_20(stairs):
    raw_counts = [day for days in stairs for day in days]
    return sum(raw_counts) * 20
