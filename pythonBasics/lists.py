#lists in python 
l1=["helo","world","this","string"]
l2=[1,2,3]
for i in l1:
  print(i)
print("length of list is")
print(len(l1))
print(l1[-1])
print(l1[3])
if "hello" in l1:
  print("hello is present in list")
else:
  print("Not present")
l1.extend(l2)
for i in l1:
  print(i)
l1.remove("helo")
'''for i in l1:
  print(i)'''
l1.pop(3)
for i in l1:
  print(i)