import re
fobj= open("C:/Users/91875/VScode/python/regex/email.txt")

for line in fobj:
    pattern=r'From\s([a-zA-Z\_\.]+@[a-zA-Z\_\.]+)';
    found=re.search(pattern,line);
    print(found.group(1));

fobj.close();