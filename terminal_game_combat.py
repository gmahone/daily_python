def combat(health, damage):
    result = health - damage
    return result if result >= 0 else 0 
