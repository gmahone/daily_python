def contamination(text, char):
  result_len = len(text)
  return char*result_len


# using import re
import re
def contamination(text, char):
  return re.sub(".", char, text)


# lambda function
contamination=lambda t,c: c*len(t)

# with types
def contamination(text: str, char: str) -> str:
    return char * len(text)
