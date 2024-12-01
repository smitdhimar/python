#this is the program to make a list of lengths of words in a string using list comprehension only but all this if not the in string;

str="this is the string in which there are 33 words but the answer will be 27 since the word the is not counted and the word the is 6 times in this sentence"

l=len([len(x) for x in str.split() if x!='the'])
# print(len(l)) #this should be 26
print(l)