import os as os;

#creating objects for opening files

# print(os.getcwd())
folderPath="C:/Users/91875/VScode/python/FiileIO/";
numberFile= open(folderPath+"numbers.txt");
negativeFile=open(folderPath+"negative.txt", "w+")
positiveFile=open(folderPath+"positive.txt", "w+")

# Reading from the number file
for num in numberFile:
    if(num>0):
        positiveFile.write(str(num));
    else:
        negativeFile.write(str(num));

numberFile.close();
negativeFile.close();
positiveFile.close();