def alphabet_war(fight):
    left_score_dict = {"w" : 4, "p" : 3, "b" : 2, "s" : 1}
    right_score_dict = {"m" : 4, "q" : 3, "d" : 2, "z" : 1}
    
    left_side_score = right_side_score = 0
    
    for key, value in left_score_dict.items():
        left_side_score += fight.count(key) * value
        
    for key, value in right_score_dict.items():
        right_side_score += fight.count(key) * value
    
    print(left_side_score)
    print(right_side_score)
    pass
