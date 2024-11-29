import re

obj=open("C:/Users/91875/VScode/python/regex/cp_2020_entry.txt")
pattern=r'([a-zA-Z]+),(\d{1,2}-\d{1,2}-\d{4})';
for line in obj:
    found=re.search(pattern,line);
    print(found.group(1))
    print(found.group(2))

obj.close();