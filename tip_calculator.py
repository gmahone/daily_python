def calculate_tip(amount, rating):
    tip_dict = {"terrible": 0, "poor": 0.05, "good": 0.1, "great": 0.15, "excellent": 0.2}
    print(tip_dict[rating.lower()])
    pass
