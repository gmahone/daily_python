def stairs_in_20(stairs):
    raw_counts = [day for days in stairs for day in days]
    return sum(raw_counts) * 20

# solution using sum of sums
def stairs_in_20(stairs):
    return sum(sum(day) for day in stairs) * 20
