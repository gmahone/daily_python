def to_time(seconds):
    hours = seconds // (60*60)
    minutes = seconds % (60*60) // 60
    return f"{hours} hour(s) and {minutes} minute(s)"


# alternative
def to_time(seconds):
    return f'{seconds//3600} hour(s) and {(seconds//60)%60} minute(s)'


# solution using .format
def to_time(seconds):
    return '{} hour(s) and {} minute(s)'.format(seconds//3600,(seconds%3600)//60)


# using divmod
def to_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f'{h} hour(s) and {m} minute(s)'
