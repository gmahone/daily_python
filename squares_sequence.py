def squares(x: int, n: int) -> list[int]:
    result = []
    if n <= 0:
        return result
    while len(result) < n:
        result.append(x)
        x = x*x
    return result
    
