"""
check50 belgort-clark/example_checks/main/example_1 --local
"""

import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
  """File hello.py exists""" # this is what you will see when running check50
  check50.exists("hello.py") # the actual check
  
@check50.check(exists) # only run this check if the exists check has passed
def prints_hello():
  """Prints "Hello, World!" """
  check50.run("python3 hello.py").stdout("[Hh]ello, [Ww]orld!?\n", regex=True)

@check50.check(exists)
def gets_input():
  """Inputs the names Fred and Jim and then prints them and then prints ending message"""
  check50.run("python3 hello.py").stdin("Fred").stdout("Name: Fred").stdin("Jim").stdout("Name: Jim").stdout("Program [Ee]nded", regex=True).exit(0)
  
