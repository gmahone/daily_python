def evil(n):
    binary_count = bin(n).replace("0b", "").count("1")
    if binary_count % 2:
        return "It's Odious!"
    else:
        return "It's Evil!"
