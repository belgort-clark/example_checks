import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
  """File hello.py exists""" # this is what you will see when running check50
  check50.exists("hello.py") # the actual check
  
@check50.check(exists) # only run this check if the exists check has passed
def prints_hello():
  """Prints "hello, world!" """
  check50.run("python3 hello.py").stdout("[Hh]ello, world!?\n", regex=True)

@check50.check(exists)
def gets_input():
  """Inputs the names Fred and Jim and then prints them"""
  check50.run("python3 hello.py").stdin("Fred").stdout("Fred").stdin("Jim").stdout("Jim").stdout("Program [Ee]nded", regex=True).exit(0)
  
