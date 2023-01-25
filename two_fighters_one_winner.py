import math

def declare_winner(fighter1, fighter2, first_attacker):
    fighter1_turns = math.ceil(fighter1.health / fighter2.damage_per_attack)
    fighter2_turns = math.ceil(fighter2.health / fighter1.damage_per_attack)
    print(fighter1_turns)
    print(fighter2_turns)
    pass
