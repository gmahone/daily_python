def leo(oscar):
    result = "When will you give Leo an Oscar?"
    if oscar == 88:
        result = "Leo finally won the oscar! Leo is happy"
    if oscar == 86:
        result = "Not even for Wolf of wallstreet?!"
    if oscar > 88:
        result = "Leo got one already!"
    return result

# solution with map
def leo(oscar):
    if oscar <= 88:
        return {86: 'Not even for Wolf of wallstreet?!',
                88: 'Leo finally won the oscar! Leo is happy'}.get(
            oscar, 'When will you give Leo an Oscar?')
    return 'Leo got one already!'
