def to_time(seconds):
    hours = seconds // (60*60)
    minutes = seconds % (60*60) // 60
    return f"{hours} hour(s) and {minutes} minute(s)"
