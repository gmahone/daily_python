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


## other solutions

def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]

def productFib(prod):
    func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
    return func(0, 1)
