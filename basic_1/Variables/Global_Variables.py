# Variables that are created outside of a function  are known as global variables

from basic_1.Variables import Output_Variables
a="good day"
def myfunc():
 print("have a " + a)

myfunc()
  

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
