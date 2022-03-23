def productFib(prod):
    Fn = [0,1]
    i = 1
    while True:
        Fnew = Fn[i-1] + Fn[i]
        if Fn[i-1] * Fn[i] < prod:
            Fn.append(Fnew)
            i += 1
        elif Fn[i-1] * Fn[i] > prod:
            return [Fn[i-1], Fn[i], False]
        else:
            return [Fn[i-1], Fn[i], True]
          
print(fibonacci_prod(714))
print(fibonacci_prod(800))
