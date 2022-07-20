import re

def validate_code(code):
    return bool(re.findall("^[123]", str(code)))


# non regex solution
def validate_code(code):
    return str(code).startswith(('1', '2', '3'))


# non regex solution
def validate_code(code):
    return str(code)[0] in '123'

# add re solution using match
import re

def validate_code(code):
    return bool(re.match("^[1-3]",str(code)))
