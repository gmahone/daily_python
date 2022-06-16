def combat(health, damage):
    result = health - damage
    return result if result >= 0 else 0 

# other solutions

# solution using max
def combat(health, damage):
    return max(0, health - damage)

# similar formulation as original solution
def combat(health, damage):
    return health - damage if health > damage else 0
