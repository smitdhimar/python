import re
input_string = "Name: John, Marks: 85; Name: Alice, Marks: 92; Name: Bob, Marks: 78"

pattern=r'Name:\s(\w+),\sMarks:\s(\d+)'

matches=re.findall(pattern, input_string)
print(matches)
for i in matches:
    print(i[0])
    print(i[1]);