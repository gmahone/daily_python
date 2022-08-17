def get_drink_by_profession(param):
    result_dict = {"Jabroni": "Patron Tequila",
                  "School Counselor": "Anything with Alcohol",
                  "Programmer": "Hipster Craft Beer",
                  "Bike Gang Member": "Moonshine",
                  "Politician": "Your tax dollars",
                  "Rapper": "Cristal"}
    result = result_dict[param] if result_dict[param] else "Beer"
    return result
