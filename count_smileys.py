import re

def count_smileys(arr):
    result = []
    for i in arr:
        tmp = re.findall("[:;]+[-~]?[)D]+", i)
        if len(tmp) > 0:
            result.append(tmp)
    return len(result)

# add other solutions

from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

# very deliberate solution -  all possible combos tested
# but for this solution, don't need to import
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count


import re

def count_smileys(arr):
    return sum(1 for s in arr if re.match(r'\A[:;][-~]?[)D]\Z',s))


def count_smileys(arr):
    smiles = set([a+b+c for a in ":;" for b in ['','-', '~'] for c in ")D"])
    return len([1 for s in arr if s in smiles])


count_smileys=lambda a:sum(s and s[0]in':;'and s[-1]in')D'and s[1:-1]in('','-','~')for s in a)


import re
def count_smileys(arr):
    count = 0
    for smiley in arr:
        count += len(re.findall('[:;][-~]?[)D]', smiley))
    return count
