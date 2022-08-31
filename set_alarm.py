def set_alarm(employed, vacation):
    return True if employed and not vacation else False


## non explicit return
def set_alarm(employed, vacation):
    return employed and not vacation


# solution with cases
def set_alarm(employed, vacation):
    if employed:
        if vacation:
            return False
        return True
    return False


# lambda function
set_alarm=lambda *a:a==(1,0)


# case testing and using is False
def set_alarm(employed, vacation):
    if employed and vacation is False:
        return True
    else:
        return False
