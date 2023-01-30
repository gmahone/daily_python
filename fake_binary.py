def fake_bin(x):
    result = ["0" if int(i) < 5 else "1" for i in x]
    return "".join(result)
