import re

def validate_code(code):
    return bool(re.findall("^[123]", str(code)))


# non regex solution
def validate_code(code):
    return str(code).startswith(('1', '2', '3'))
