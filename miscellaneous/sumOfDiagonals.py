
arr= [[1,2,3],[4,5,6],[6,7,8]];
leftDiag,rightDiag=0,0
for i in range(0, len(arr)):
    for j in range(0,3):
        if(i==j):
            leftDiag+= arr[i][j];
        if(i+j==2):
            rightDiag+=arr[i][j];

print(leftDiag);
print(rightDiag)