def get_drink_by_profession(param):
    result_dict = {"jabroni": "Patron Tequila",
                  "school counselor": "Anything with Alcohol",
                  "programmer": "Hipster Craft Beer",
                  "bike gang member": "Moonshine",
                  "politician": "Your tax dollars",
                  "rapper": "Cristal"}
    try: 
        return result_dict[param.lower()]
    except:
        return "Beer"
    return result
