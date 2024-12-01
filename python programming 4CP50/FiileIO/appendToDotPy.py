import os;

str=input("please enter string tobe written in existing file: ");
folderPath="C:/Users/91875/VScode/python/FiileIO/";

file=open(folderPath+"seperateNumbers.py","a+");
fil=open(folderPath+"numbers.txt","a+");
file.seek(0,2);
file.write(str);
file.seek(0,0)
for line in file:
    # print()
    print(line);

fil.seek(0,0)
for line in fil:
    print(line);
file.close();
