#MODULE FOR REGULAR EXPRESSIONS
import re

defaultString = "this is the default string we are having what we will do is check the given string is there in default string or not"
x = re.search(r"this.*not", defaultString)
if x:
  print("present")
  print(x.start())
  print(x.end())
else:
  print("Not present")

#find all the "is" substring in list
x = re.findall("is", defaultString)
print(x)

# find all the words and convert them to set from list and print every unique word in default strin
x = re.split("\s", defaultString)
x1 = set(x)
for i in x1:
  print(i)

print("\n")

#find the multitime occuring words
y=list(x1)
print()
