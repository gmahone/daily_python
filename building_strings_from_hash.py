def solution(pairs):
    result = [f"{key} = {value}" for key,value in pairs.items()]
    return ",".join(result)
