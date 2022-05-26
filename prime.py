x=int(input("Enter any number-->"))
b=0
for i in range (1,x+1):
    if x%i==0:
        b+=1
if b==2:
        print(x,"is prime number")
else:
        print(x,"is not prime number")