import math

def declare_winner(fighter1, fighter2, first_attacker):
    fighter1_turns = math.ceil(fighter1.health / fighter2.damage_per_attack)
    fighter2_turns = math.ceil(fighter2.health / fighter1.damage_per_attack)
    if fighter1_turns > fighter2_turns:
        return fighter1.name
    elif fighter2_turns > fighter1_turns:
        return fighter2.name
    else:
        return first_attacker

# another solution
def declare_winner(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:        
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name
