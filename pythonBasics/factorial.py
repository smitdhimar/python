def fact(num):
  if(num>0):
    return num*fact(num-1)
  if(num==0):
    return 1
num=int(input("enter the number to get it's factorial: "))
print("factorial:",fact(num))