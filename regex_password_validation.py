regex="^(?=.{6,}$)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(^[A-Za-z0-9]+$)"

# clearly labeled solution using re
from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)
