class List:
    def remove_(self, integer_list, values_list):
        result = []
        for i in integer_list:
            if i not in values_list:
                result.append(i)
        return result

# one line solution
class List(object):
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]
