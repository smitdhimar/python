l1 = ["item1", "item2", "item3", "item4"]
l3 = ["57", "24", "48", "1"]
l2 = [x for x in l1]

for x in l2:
  print(x)

for x in l3:
  l2.append(x)

print("printing list again")
for x in l2:
  print(x)
  
print("sorting the list")
l2.sort(key=str.lower)
for x in l2:
  print(x)