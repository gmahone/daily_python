def boredom(staff):
    assessment_score = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25,    
    }
    score = 0
    for department in staff.values():
        score += assessment_score[department]
    if score > 100:
        return "party time!!"
    elif score > 80:
        return "i can handle this"
    else:
        return "kill me now"
