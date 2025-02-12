#Create a Module
def greeting(name):
  print("Hello, " + name)


#Variables in Module
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

"""import mymodule

a = mymodule.person1["age"]
print(a)"""

#Re-naming a Module
"""import mymodule as mx

a = mx.person1["age"]
print(a)"""


#Built-in Modules
import platform

x = platform.system()
print(x)


#Using the dir() Function
import platform

x = dir(platform)
print(x)


#Import From Module
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "Akbota",
  "age": 18,
  "country": "Kazakhstan"
}