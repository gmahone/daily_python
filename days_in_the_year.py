def year_days(year):
    result = "{} has 365 days".format(year)
    if not year % 4:
        result = "{} has 366 days".format(year)
    if not year % 100 and year % 400:
        result = "{} has 365 days".format(year)
    return result

# a different solution
def year_days(year):
    days = 365
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days += 1
    return "%d has %d days" % (year, days)
