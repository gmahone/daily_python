def warn_the_sheep(queue):
    wolf_index = len(queue) - queue.find("wolf")
    if wolf_index == 1:
        result = "Pls go away and stop eating my sheep"
    else:
        result = `Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!`
    return result
