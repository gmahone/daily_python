def evil(n):
    binary_count = bin(n).replace("0b", "").count("1")
    if binary_count % 2:
        return "It's Odious!"
    else:
        return "It's Evil!"

# another solution
def evil(n):
    return "It's Evil!" if  bin(n).count('1')%2 == 0 else "It's Odious!"
