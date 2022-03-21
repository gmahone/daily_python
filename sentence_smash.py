def sentence_smash(words):
    sentence = ""
    for i in range(0, len(words)):
        sentence = sentence + words[i]
        if(i < len(words)-1):
            sentence = sentence + " "
    return sentence


test = ["this","is","a","test"]

print(sentence_smash(test))
