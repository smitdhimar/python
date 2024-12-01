list=[]
def loArgs(*args):
  for i in args:
    list.append(i)

def printL():
  for i in list:
    print(i)

loArgs("smit","animeshkumar","dhimar")
printL()