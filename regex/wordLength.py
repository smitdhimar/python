import re
str="man mone meh meh meh on a mission on manhattan"

found=re.findall(r'\bm\w{2}\b', str)
print(found)