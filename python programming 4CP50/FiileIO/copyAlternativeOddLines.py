import os;

folderPath="C:/Users/91875/VScode/python/FiileIO/"
data=open(folderPath+"bvm_cp.txt");
target=open(folderPath+"final_cp.txt","a+");


i=1
for line in data:
    if(int(i%2)!=0):
        target.write(line);
    i=i+1;

target.seek(0,0);
for line in target:
    print(line,);
data.close();
target.close();