def array(string):
    result = string.split(",")
    return None if len(result) < 3 else " ".join(result[1:-1])

# solution with less separation
def array(string):
  return " ".join(string.split(",")[1:-1]) or None
