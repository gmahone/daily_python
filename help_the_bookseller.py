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
