def shorter_reverse_longer(a,b):
  longer = a
  shorter = b
  if len(b) > len(a):
    longer = b
    shorter = a
  result = shorter + longer[::-1] + shorter
  return result


# multi assign
def shorter_reverse_longer(a,b):
  if len(a) < len(b): a, b = b, a
  return b+a[::-1]+b
