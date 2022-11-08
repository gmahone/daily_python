def seven_ate9(str_):
    result = str_
    while "797" in result:
        result = "77".join(result.split("797"))
    return result

# using find and replace
def seven_ate9(str_):
   while str_.find('797') != -1:
       str_ = str_.replace('797','77')
   return str_
