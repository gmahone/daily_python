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


## dict outside of function
d = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
}

def get_drink_by_profession(s):
    return d.get(s.lower(), "Beer")


## string search in return using title case
def get_drink_by_profession(param):
    return {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }.get(param.title(), "Beer")


## if else for string search
def get_drink_by_profession(param):
    d = {"Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol", "Programmer":"Hipster Craft Beer", "Bike Gang Member":"Moonshine", "Politician":"Your tax dollars", "Rapper":"Cristal"}
    if param.title() in d:
        return d[param.title()]
    else:
        return "Beer"

    
## longform via elif
def get_drink_by_profession(param):
    newparam = param.lower()
    if newparam == 'jabroni':
        return 'Patron Tequila'
    elif newparam == 'school counselor':
        return 'Anything with Alcohol'
    elif newparam == 'programmer':
        return 'Hipster Craft Beer'
    elif newparam == 'bike gang member':
        return "Moonshine"
    elif newparam == 'politician':
        return "Your tax dollars"
    elif newparam == "rapper":
        return "Cristal"
    else:
        return "Beer"
