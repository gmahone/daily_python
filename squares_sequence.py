def squares(x: int, n: int) -> list[int]:
    result = []
    if n <= 0:
        return result
    while len(result) < n:
        result.append(n)
        n = n*n
    return result
    
