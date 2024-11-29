import re
str= "this is fox si foxes asdf asd "
found=re.findall(r'fox\w+',str);
print(found)