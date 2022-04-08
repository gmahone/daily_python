

# def test_int(self):
#     with self.assertRaises(ValueError):
#         test_val = int(test)

# test = ("net" + "###") *3
# if int("abc"), ValueError:
#     test = "Yes"
# print(test)
# def appender(in_list, new_value, desired_length):
#     if len(in_list) == desired_length:
#         result =  in_list
#     else:
#         in_list.append(new_value)
#         result = appender(in_list, new_value, desired_length)
#     return result


# def prefill(n, v):
#     try:
#         n = int(n)
#     except ValueError:
#         print(n + " is invalid")
#     else:
#         result = appender(in_list = [v], new_value = v, desired_length = n)
#         return result


# print(prefill(n = 2,v = "abc"))
# print(prefill("xyz", 1))
# print(prefill(0, "abc"))
# test = []
# print(len(test))


# def appender(in_list, new_value, desired_length):
#     if len(in_list) == desired_length:
#         result =  in_list
#     else:
#         next_list = in_list.append(new_value)
#         result = appender(next_list, new_value, desired_length)
#     return result


# def prefill(n, v):
#     result = appender(in_list = [v], new_value = v, desired_length = n)
#     return result




# def appender(in_list, new_value, desired_length):
#     if len(in_list) == desired_length:
#         result =  in_list
#     else:
#         in_list.append(new_value)
#         result = appender(in_list, new_value, desired_length)
#     return result


# def prefill(n, v = "abc"):
#     if n == 0 or n == "0":
#         return []
#     if isinstance(n, float):
#         raise TypeError(str(n) + " is invalid")
#     try:
#         n = int(n)
#     except ValueError:
#         print(n + " is invalid")
#     else:
#         if n < 0:
#             raise TypeError(str(n) + " is invalid")
#         else:
#             result = appender(in_list = [v], new_value = v, desired_length = n)
#             return result

# print(prefill(0, "abc"))
# print(prefill(0.1, "abc"))


def appender(in_list, new_value, desired_length):
    if len(in_list) == desired_length:
        result =  in_list
    else:
        in_list.append(new_value)
        result = appender(in_list, new_value, desired_length)
    return result


def prefill(n, v = "abc"):
    if isinstance(n, int) or not isinstance(n, float) and int(n):
        result = appender(in_list = [v], new_value = v, desired_length = n)
        return result
    else:
        raise TypeError(str(n) + "is invalid")

# print(prefill(0, "abc"))
# print(prefill(0.1, "abc"))



def prefill(n, v):
    if type(v) != list:
        v = [v]
    if len(v) >= n:
        result = v
    else:
        v.append(v[0])
        result = prefill(n, v)
    return result
