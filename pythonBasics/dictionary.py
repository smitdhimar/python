#dictionaries
# dict = {"brand": "hyundai", "model": "eon", "subModel": "xsmax"}
# print(dict["brand"] + " " + dict["model"] + " " + dict["subModel"])

thisdict = dict(brand="mahindra", model="XUV", subModel="5oo")
print(thisdict)
x = thisdict.get("brand")
print(x)
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)

print("\nlooping through dictionaries:")
for i in thisdict:
  print(i + ": " + thisdict[i])
