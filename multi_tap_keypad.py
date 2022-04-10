def presses(phrase):
    pad = ["ABC2","DEF3","GHI4","JKL5","MNO6","PQRS7","TUV8","WXYZ9"," 0"]
    type_dict = {}
    for i in pad:
        for j in range(0, len(i)):
           type_dict.update({i[j]: (j+1)})
    presses = 0
    for i in phrase:
        presses += type_dict[i.upper()]
    return presses
