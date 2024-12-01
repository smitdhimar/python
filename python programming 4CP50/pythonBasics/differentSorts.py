#ps: find a sorted list that ordered as numbers ordered to more closer to 50
list = [57, 87, 21, 49, 17, 37, 45, 65]


def fun(n):
  return abs(n - 50)


list.sort(key=fun)
for i in list:
  print(i)
#now find a sorted list farthest to number 52
print("\n new sort")
def fun1(n):
  return (500-abs(n-52))

list.sort(key=fun1)
for i in list:
  print(i)


#sort list based on a square, note that negative numbers will be having positive square
print("\nnewlist")
list=[4,5,-7,-3,6,-4,8]
def fun2(n):
  return n*n
list.sort(key=fun2)
for i in list:
  print(i)
