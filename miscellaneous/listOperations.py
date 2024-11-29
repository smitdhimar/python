# given the list perform the insert delete operations without built in methods

l=[9,8,7,6,5,4,3];

# insert 10 at first;
# l.append(0);
# for i in range(0,7):
#     l[7-i]=l[7-i-1];
# l[0]=10
l=[10]+l;
# print(l)
l=l+[2]

l=l[:5]+l[6:];

print(l[::-1])


