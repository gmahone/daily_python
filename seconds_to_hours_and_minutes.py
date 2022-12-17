def to_time(seconds):
    hours = seconds // (60*60)
    minutes = seconds % (60*60) // 60
    return f"{hours} hour(s) and {minutes} minute(s)"


# alternative
def to_time(seconds):
    return f'{seconds//3600} hour(s) and {(seconds//60)%60} minute(s)'
