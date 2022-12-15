leet_dict = {
  "A" : '@',
  "B" : '8',
  "C" : '(',
  "E" : '3',
  "G" : '6',
  "H" : '#',
  "I" : '!',
  "L" : '1',
  "O" : '0',
  "S" : '$',
  "T" : '7',
  "Z" : '2'
}

def to_leet_speak(str):
    for key, value in leet_dict.items():
        str = value.join(str.split(key))
    return str

  
# solution using translate
def to_leet_speak(str):
    return str.translate(str.maketrans("ABCEGHILOSTZ", "@8(36#!10$72"))
