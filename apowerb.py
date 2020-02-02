# MD-SHADAAB-FARHAN
# code to find a power b in O(log(b)) time.
a=int(input())
b=int(input())
res=1
x=a
while(b>0):
    if(b&1==1):
        res=res*x
    x=x*x
    b=b>>1
print(res)
