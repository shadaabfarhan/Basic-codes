import math
n=int(input())
c=0
l=math.ceil(math.sqrt(n))
for i in range(1,l):
    if(n%i==0):
        c+=2
if(n==1): #if n=1 ,no.of divisors=1
    print(1)
else:
    print(c)
    
