from array import *

a = array('i', [4, 5, 6, 7])

for i in a:
  print(i)
#creating arrray b from a by doing changing in all elements
b=array(a.typecode,(i*2 for i in a))
        
print("for array b")
for i in b:
  print(i)

print("for array a")
for i in range(len(a)):
  print(a[i])

#slicing of the arrays 
#array a
#print only 2 to 3 elements of array a
print(a[1:3])