def to_freud(sentence):
  return " ".join(["sex" for i in (sentence.split(" "))]) if sentence else ""
