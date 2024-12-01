s = {"unordered", "unindexed", "unchangeable", "no duplicates"}
print("unindexed" in s)
s1 = {"element"}
s.update(s1)
s.discard("element")
for i in s:
  print(i)
x = s.pop()
print("\n" + x)
print(s)
print(s1)
s.update(s1)
print(s)
# print(s1)
