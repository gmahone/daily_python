def lovefunc( flower1, flower2 ):
    flower1_test = flower1 % 2 == 0
    flower2_test = flower2 % 2 == 0

    if flower1_test and not flower2_test:
        return True
    elif flower2_test and not flower1_test:
        return True
    else:
        return False


print(lovefunc(5, 5))
print(lovefunc(4,5))
print(lovefunc(7,2))
