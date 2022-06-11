def say_hello(name):
  return "Hello, " + name

# other solutions

# template literal solution
def say_hello(name):
    return f"Hello, {name}"

# solution using .format
def say_hello(name):
    return "Hello, {}".format(name)
