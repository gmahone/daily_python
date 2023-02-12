def solution(pairs):
    result = [f"{key} = {value}" for key,value in pairs.items()]
    result = sorted(result)
    return ",".join(result)


# single line solution
def solution(pairs):
    return ','.join(sorted([ f'{key} = {value}' for key,value in pairs.items() ]))
