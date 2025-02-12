#JSON in Python
import json
x =  '{ "name":"Bota", "age":18, "city":"Almaty"}'
y = json.loads(x)
print(y["age"])


#Convert from Python to JSON
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)

#Python	JSON
#dict	Object
#list	Array
#tuple	Array
#str 	String
#int	Number
#float	Number
#True	true
#False	false
#None	null

#Example
import json

x = {
  "name": "Akbota",
  "age": 18,
  "married": True,
  "divorced": False,
  "children": ("Anar","Aisha"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#Format the Result
json.dumps(x, indent=4)

#Example
json.dumps(x, indent=4, separators=(". ", " = "))


#Order the Result
json.dumps(x, indent=4, sort_keys=True)