#write a function to print the primes numbers in the given range;

#function for checking one number
def prime(num):
    for i in range(2, int(num/2)+1):
        if(int(num%i)==0):
            return False;
    return True;

#looping through the range and checking each number whether it is prime or not 
def Range(low,high):
    for i in range(low, high+1):
        if(prime(i)):
            print(i)

# calling range function and getting the user input at the same time
Range( int(input("enter  low: ")), int(input("enter high ")));