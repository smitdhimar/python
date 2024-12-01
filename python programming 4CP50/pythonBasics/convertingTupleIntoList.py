#declaring a tuple
tup = ("hello", 89, True)
l1 = list(tup)
l1.append("newstring")
for i in l1:
  print(i)

print(l1)
#converting again to tuple
tup = tuple(l1)
print("tuple")
print(tup)

print("loop through tuple")
for i in range(len(tup)):
  print(tup[i])
