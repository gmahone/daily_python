def switcher(arr):
    translation_dict = {
        "26": "a",
        "25": "b",
        "24": "c",
        "23": "d",
        "22": "e",
        "21": "f",
        "20": "g",
        "19": "h",
        "18": "i",
        "17": "j",
        "16": "k",
        "15": "l",
        "14": "m",
        "13": "n",
        "12": "o",
        "11": "p",
        "10": "q",
        "9": "r",
        "8": "s",
        "7": "t",
        "6": "u",
        "5": "v",
        "4": "w",
        "3": "x",
        "2": "y",
        "1": "z",
        "27": "!",
        "28": "?",
        "29": " "
    }
    return "".join([translation_dict[i] for i in arr])


# different dict building
def switcher(arr):
    d = {str(i): chr(123-i) for i in range(1,27)}
    d.update({'27':'!'})
    d.update({'28':'?'})
    d.update({'29':' '})
    d.update({'0':''})
    return ''.join([d[str(i)] for i in arr])
