import json
#CONVERT JSON TO PYTHON AND USE
x = '{"name":"smit","email":"smitdhimar23@gmail.com","password":"Smit@123"}'
y = json.loads(x)
print(y["name"])
print(y)

#CONVERT PYTHON DICTIONARY INTO JSON FORMAT
x = {"name": "smit", "email": "smitdhimar23@gmail.com", "password": "Smit@123"}
y = json.dumps(x, indent=4, sort_keys=True)
print(y)
#indent as an arguement
#sort_keys function sorts the keys in object
