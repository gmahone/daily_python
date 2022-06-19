def stock_list(listOfArt, listOfCat):
    art_dict = {}
    for i in listOfArt:
        split_temp = i.split(" ")
        if i[0][0] in art_dict:
            art_dict[i[0][0]] += int(i[1])
        else:
            art_dict[i[0][0]] = int(i[1])
