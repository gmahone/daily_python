import re

def validate_code(code):
    return bool(re.findall("^[123]", str(code)))
