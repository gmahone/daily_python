def shorter_reverse_longer(a,b):
  longer = a
  shorter = b
  if len(b) > len(a):
    longer = b
    shorter = a
  result = shorter + rev(longer) + shorter
  print(result)
  pass
