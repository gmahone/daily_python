def remove_rotten(bag_of_fruits):
    print(["rotten" in i for i in bag_of_fruits])
    result = [i.replace("rotten", "") for i in bag_of_fruits]
    print(result)
    pass
