def warn_the_sheep(queue):
    wolf_index = len(queue) - queue.index("wolf") - 1
    if wolf_index == 0:
        result = "Pls go away and stop eating my sheep"
    else:
        result = f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!"
    return result

# using the 
def warn_the_sheep(queue):
    wolf_index = len(queue) - queue.index("wolf") - 1
    return f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!" if wolf_index else "Pls go away and stop eating my sheep"
  
