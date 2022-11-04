def contamination(text, char):
  result_len = len(text)
  return char*result_len


# using import re
import re
def contamination(text, char):
  return re.sub(".", char, text)
