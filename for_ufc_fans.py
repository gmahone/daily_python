def quote(fighter):
    if fighter.lower() == "george saint pierre":
        return "I am not impressed by your performance."
    elif fighter.lower() == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return "Please either George Saint Pierre or Conor McGregor"


# add solution with pre-defined statement
statements = {
    'george saint pierre': "I am not impressed by your performance.",
    'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"
}

def quote(fighter):
    return statements[fighter.lower()]


## solution using get
