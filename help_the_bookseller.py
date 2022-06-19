def stock_list(listOfArt, listOfCat):
    art_dict = {}.fromkeys(listOfCat, 0)
    for i in listOfArt:
        split_temp = i.split(" ")
        if split_temp[0][0] in art_dict:
            art_dict[split_temp[0][0]] += int(split_temp[1])
    result = []
    for k,v in art_dict.items():
        result.append(f'({k} : {v})')
    return " - ".join(result) if len(listOfArt) != 0 else ''


# other solutions
def stock_list(listOfArt, listOfCat):
    if listOfArt and listOfCat:
        return " - ".join(['(%s : %d)' % (c, sum([int(i.split(" ")[1]) for i in listOfArt if c == i[0]])) for c in listOfCat])
    else:
        return ""

    
#
def stock_list(listOfArt, listOfCat):
    if not listOfArtt or not listOfCat:
        return ""
    return " - ".join(
        "({} : {})".format(
            listOfCat,
            sum(int(item.split()[1]) for item in listOfArt if item[0] == listOfCat))
        for listOfCat in listOfCat)
