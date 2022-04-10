def presses(phrase):
    pad = ["1","*","#","ABC2","DEF3","GHI4","JKL5","MNO6","PQRS7","TUV8","WXYZ9"," 0"]
    type_dict = {}
    for i in pad:
        for j in range(0, len(i)):
           type_dict.update({i[j]: (j+1)})
    presses = 0
    for i in phrase:
        print(i)
        if i.isalnum() or i == " " or i == "*" or i == "#":
            print(i)
            presses += type_dict[i.upper()]
    return presses

# add other solutions

BUTTONS = [ '1',   'abc2',  'def3',
          'ghi4',  'jkl5',  'mno6',
          'pqrs7', 'tuv8', 'wxyz9',
            '*',   ' 0',    '#'   ]
def presses(phrase):
    return sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button)


buttons = [
    '1',
    'abc2',
    'def3',
    'ghi4',
    'jkl5',
    'mno6',
    'pqrs7',
    'tuv8',
    'wxyz9',
    '*',
    ' 0',
    '#'
]
def getPresses(c):
    for button in buttons:
        if c in button:
            return button.index(c) + 1
    return 0

def presses(phrase):
    return sum(getPresses(c) for c in phrase.lower())


def presses(phrase):
    x = 0
    for letter in phrase:
        if letter.lower() in list('1*#adgjmptw '): x+= 1
        elif letter.lower() in list('0behknqux'): x+= 2
        elif letter.lower() in list('cfilorvy'): x+= 3
        elif letter.lower() in list('234568sz'): x+= 4
        elif letter.lower() in list('79'): x+= 5
    return x


def presses(phrase):
    numbers = ['*','#','1','ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', ' 0']
    print(phrase)
    phrase = phrase.upper()
    result = 0
    
    for letter in phrase:
        for n in numbers:
            if letter in n:
                result = result + n.index(letter) + 1
    return result


presses = lambda s: sum((c in b) * (1 + b.find(c)) for c in s.lower() for b in
               '1,abc2,def3,ghi4,jkl5,mno6,pqrs7,tuv8,wxyz9,*, 0,#'.split(","))
