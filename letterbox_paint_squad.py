def paint_letterboxes(start, finish):
    number_list = list(range(start, finish+1))
    concat_numbers = ""
    for i in number_list:
        concat_numbers += str(i)
    result = [concat_numbers.count(str(n)) for n in range(0,10)]
    return result


# alternative solution
def paint_letterboxes(start, finish):
    xs = [0] * 10
    for n in range(start, finish+1):
        for i in str(n):
            xs[int(i)] += 1
    return xs
