def _if(bool, func1, func2):
    return func1() if bool else func2()

# alternative calling
def _if(bool, func1, func2):
  (bool and func1 or func2)()
