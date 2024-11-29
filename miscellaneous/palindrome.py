a= int(input("enter your number: "));
print(f"the number you entered is {a}");

original  =a;
newNum=0;

while(a!=0):
    rem = int(a%10);
    print(rem)
    newNum = newNum*10 + rem;
    a= int(a/10)

if(newNum==original):
    print("yes")
else:
    print("no");
    print(newNum)