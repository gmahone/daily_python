def no_boring_zeros(n):
    if not n:
        return n
    elif n % 10:
        return n
    else:
        n = int(n/10)
        return no_boring_zeros(n)

# string stripping solution
def no_boring_zeros(n):
    try:
        return int(str(n).rstrip("0"))
    except ValueError:
        return 0

# string strip using if else
def no_boring_zeros(n):
  return int(str(n).rstrip("0")) if n else n
