def sort_gift_code(code):
  return "".join(sorted(list(code)))


# shorter solution without making list
def sort_gift_code(code):
    return "".join(sorted(code))

# lambda version
sort_gift_code = lambda code: ''.join(sorted(code))
