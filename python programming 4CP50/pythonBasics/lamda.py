#lambda functions are used for of anonyomous calls
#practice on lamda functions
#can have many argument but only one expression
a = 8
b = 9
c = 3
# x=lambda a,b,c:a+b+c
# print(x(a,b,c))
l1 = []
lis = [2, 8, 7, 5, 6, 7, 9, 10]
x = lambda a: a * a
for i in lis:
  l1.append(x(i))

for i in l1:
  print(i)

l1 = list(map(lambda x: x * x * x, lis))
print(l1)

l2 = list(filter(lambda x: x % 2 == 0, l1))
print(l2)

a = lambda x: x * x
for i in l2:
  l1.append(a(i))

print(l1)
