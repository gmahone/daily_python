def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    result = [i.replace("rotten", "").lower() for i in bag_of_fruits]
    return result
