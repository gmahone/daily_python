def sum_all_in_range(x,y):
    return sum(range(min(x,y), max(x,y)+1))


print(sum_all_in_range(1,4))
print(sum_all_in_range(4,1))
print(sum_all_in_range(-3,3))
print(sum_all_in_range(4,4))


# other solutions

def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
