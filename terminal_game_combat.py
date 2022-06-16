def combat(health, damage):
    result = health - damage
    return result if result >= 0 else 0 

# other solutions

# solution using max
def combat(health, damage):
    return max(0, health - damage)
