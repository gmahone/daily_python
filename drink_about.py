def people_with_age_drink(age):
    if age < 14:
        drink = "toddy"
    elif age < 18:
        drink = "coke"
    elif age < 21:
        drink = "beer"
    else:
        drink = "whisky"
    return f"drink {drink}"
