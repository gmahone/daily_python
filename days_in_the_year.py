def year_days(year):
    result = "{} has 365 days".format(year)
    if not year % 4:
        result = "{} has 366 days".format(year)
    return result
        
