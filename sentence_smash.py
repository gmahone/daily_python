def sentence_smash(words):
    sentence = ""
    for i in range(0, len(words)):
        sentence = sentence + words[i]
        if(i < len(words)-1):
            sentence = sentence + " "
    return sentence


test = ["this","is","a","test"]

print(sentence_smash(test))


# add other solutions

def smash(words):
    return " ".join(words)

def smash(words):
    i=0
    l=len(words)
    str1=""
    while i<l:
        if i<l-1:
            str1+=words[i] + " "
        else: 
            str1+=words[i]
        i+=1
    return str1
