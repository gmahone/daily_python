def say_hello(name):
  return "Hello, " + name

# other solutions

# template literal solution
def say_hello(name):
    return f"Hello, {name}"

# solution using .format
def say_hello(name):
    return "Hello, {}".format(name)

# another .format
def say_hello(name):
  return "Hello, {0}".format(name)


# using %s
def say_hello(name):
    return "Hello, %s" % name

# using .__add__
say_hello = "Hello, ".__add__
