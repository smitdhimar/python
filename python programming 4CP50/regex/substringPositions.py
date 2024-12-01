import re

str="tis is fucking main string is is isi asldf asid aslkjfis ";
substring="is"

found=re.finditer(substring,str);
positions = [match.start() for match in found];
print(positions)