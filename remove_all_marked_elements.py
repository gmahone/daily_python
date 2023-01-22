class List:
    def remove_(self, integer_list, values_list):
        result = []
        for i in integer_list:
            for i not in values_list:
                result.append(i)
        return result
