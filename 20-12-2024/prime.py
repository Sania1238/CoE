#performed in jupiter notebook
def isp(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
   
   
def checking(l):
    p=[]
    for num in range(2,l+1):
        if isp(num):
            p.append(num)
    return p


l=50
c=checking(l)
print(c)
