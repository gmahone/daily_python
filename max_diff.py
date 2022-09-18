def max_diff(lst):
    return max(lst) - min(lst) if lst else 0


## similar solution using defaults
def max_diff(lst):
    return max(lst, default = 0) - min(lst, default = 0)
