## not working version here

str = "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
we = [1, 4, 4, 5, 2, 1]


# test code
#rank_dict = {}
#name_list = str.split(",")
#for i in range(0,len(name_list)):
#    curr_name = name_list[i]
#    word_value = len(curr_name)
#    for curr_letter in curr_name:
#        word_value += ord(curr_letter.upper())-64
#    rank_dict[curr_name] = word_value * we[i]
#sorted(rank_dict.items(), key=lambda x:x[1])

# occurrences = lambda s, lst: (i for i,e in enumerate(lst) if e == s)
# list(occurrences(1, [1,2,3,1])) # = [0, 3]

## print(dict(sorted(rank_dict.items(), key=lambda item: item[0])))
## print(dict(sorted(rank_dict.items(), key=lambda x:x[1])))

# print(sorted(rank_dict.items(), key=lambda x:x[1])[3][1])
## print(list(rank_dict.keys())[list(rank_dict.values()).index(172)])
#print(list(rank_dict.values()).index(172))

## working version below
# works for rank sort but not final sort
# takes first tie alphabet sorted entry rather than nth
#rank_list = []
#name_list = str.split(",")
#for i in range(0,len(name_list)):
#    curr_name = name_list[i]
#    word_value = len(curr_name)
#    for curr_letter in curr_name:
#        word_value += ord(curr_letter.upper())-64
#    rank_list.append((curr_name,word_value * we[i]))
#rank_list.sort(key=lambda tup: tup[1], reverse=True)
#print(rank_list)
#filtered_rank = list(filter(lambda tup: tup[1] == rank_list[n-1][1], rank_list))
#filtered_rank.sort(key=lambda tup: tup[0])
#winner = filtered_rank[0][0]
#print(winner)

# two ways
#sorted_by_second = sorted(rank_list, key=lambda tup: tup[1])
# rank_list.sort(key=lambda tup: tup[1])  # sorts in place
# filtered_rank = list(filter(lambda tup: tup[1] == 172, rank_list))
# print(filtered_rank)
# filtered_rank.sort(key=lambda tup: tup[0])
# print(filtered_rank[0][0])


#def rank(st, we, n):
#    print(len(st))
#    if len(st) == 0:
#        return "No participants"
#    rank_list = []
#    name_list = st.split(",")
#    if n > len(name_list):
#        return "Not enough participants"
#    for i in range(0,len(name_list)):
#        curr_name = name_list[i]
#        word_value = len(curr_name)
#        for curr_letter in curr_name:
#            word_value += ord(curr_letter.upper())-64
#        rank_list.append((curr_name,word_value * we[i]))
#    rank_list.sort(key=lambda tup: tup[1], reverse=True)
#    print(rank_list)
#    filtered_rank = list(filter(lambda tup: tup[1] == rank_list[n-1][1], rank_list))
#    filtered_rank.sort(key=lambda tup: tup[0])
#    winner = filtered_rank[0][0]
#    return winner
## need to sort first alphabetically then by rank, so ties will be adjudicated correctly
## this would fix lines 67 and 68 in the above solution

def rank(st, we, n):
    print(len(st))
    if len(st) == 0:
        return "No participants"
    rank_list = []
    name_list = st.split(",")
    if n > len(name_list):
        return "Not enough participants"
    for i in range(0,len(name_list)):
        curr_name = name_list[i]
        word_value = len(curr_name)
        for curr_letter in curr_name:
            word_value += ord(curr_letter.upper())-64
        rank_list.append((curr_name,word_value * we[i]))
    rank_list.sort(key=lambda tup: tup[0], reverse=False)
    rank_list.sort(key=lambda tup: tup[1], reverse=True)
    winner = rank_list[n-1][0]
    #print(rank_list)
    #filtered_rank = list(filter(lambda tup: tup[1] == rank_list[n-1][1], rank_list))
    #filtered_rank.sort(key=lambda tup: tup[0])
    #winner = filtered_rank[0][0]
    return winner


# add other solutions

def rank(st, we, n):
    if not st:
        return "No participants"
    if n>len(we):
        return "Not enough participants"
    name_score = lambda name,w: w*(len(name)+sum([ord(c.lower())-96for c in name]))
    scores= [name_score(s,we[i]) for i,s in enumerate(st.split(','))]
    scores = list(zip(st.split(','),scores))    
    scores.sort(key=lambda x: (-x[1],x[0]))
    return scores[n-1][0]



def win_num(name, weight):
    return (len(name) + sum(ord(c)-96 for c in name.lower())) * weight

def rank(st, we, n):
    if not st:      return "No participants"
    elif n>len(we): return "Not enough participants"
    else:           return sorted((-win_num(s,w),s) for s,w in zip(st.split(","), we))[n-1][1]
    
    
    
def rank(st, we, n):
    if not st: return "No participants"
    st = st.split(',')
    calc = lambda x: we[x[0]] * (len(x[1]) + sum(ord(m) - ord('a') + 1 for m in x[1].lower()))
    return sorted(sorted([m for m in enumerate(st)], key=lambda x: x[1]), key=lambda m: calc(m), reverse=True)[n - 1][1] if len(st) >= n else "Not enough participants"
