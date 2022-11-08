def seven_ate9(str_):
    result = str_
    while "797" in result:
        result = "77".join(result.split("797"))
    return result
