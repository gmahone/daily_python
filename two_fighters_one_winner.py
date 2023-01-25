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
