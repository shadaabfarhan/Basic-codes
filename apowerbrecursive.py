#a power b ,recursive approach
# Time Complexity: O(log(b))
def power(a,b):
    if(b==1):
        return (a)
    if(b==0):
        return 1
    if(b%2==0):
        ans=power(a,b//2)
        return ans*ans
    if(b%2==1):
        ans=power(a,b//2)
        return ans*ans*a
a=int(input())
b=int(input())
print(int(power(a,b)))
