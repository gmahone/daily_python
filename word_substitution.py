sentence = "elephant-rides are really fun!"

i = 0
first_char = 0
last_char = 0
out = []
curr_word = []
while i < len(sentence):
    if(sentence[i].isalpha()):
        last_char = i
        curr_word.append(sentence[i])
    else:
        word_length = last_char - first_char
        if (word_length) > 3:
            out.append(sentence[first_char] + str(word_length - 1) + sentence[last_char] + sentence[i])
            curr_word = []
        else:
            curr_word.append(sentence[i])
            out.append("".join(curr_word))
            curr_word = []
        first_char = i+1
    i+=1
print("".join(out))
