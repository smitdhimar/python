# l=[x for x in range(0,100) if x%7==0];
# print(l)
# l1=[x for x in range(0,100) if '3' in str(x)]
# print(l1)
# sum=0
# s="helllo world "
# l=[x for x in s if x==' ']
# print(len(l))
s= "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
s.lower();
l=[x for x in s if x not in ['a','e','i','o','u',' ']]
print(l)