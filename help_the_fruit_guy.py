def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    result = [i.replace("rotten", "").lower() for i in bag_of_fruits]
    return result


## smaller solution
def remove_rotten(bag_of_fruits):
    return [x.replace('rotten', '').lower() for x in bag_of_fruits] if bag_of_fruits else []
