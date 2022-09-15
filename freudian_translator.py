def to_freud(sentence):
  return " ".join(["sex" for i in (sentence.split(" "))]) if sentence else ""


## smaller solution
def to_freud(sentence):
    return ' '.join('sex' for _ in sentence.split())
