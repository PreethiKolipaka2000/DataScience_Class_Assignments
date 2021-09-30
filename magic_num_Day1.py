# PROGRAM        : MAGIC NUMBER 
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 18-SEP-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 
def find(n):
    a=[int(x) for x in str(n)]
    t=[]
    a.sort()
    mini="".join(map(str,a))
    a.sort(reverse=True)
    maxi="".join(map(str,a))
    t.append(int(mini))
    t.append(int(maxi))
    return t 

n=int(input())
flag=False
l=[]
while(n>0):
    a=find(n)
    if(a[1]-a[0] in l):
        flag=False 
        break 
    if(a[1]-a[0]==6174):
        flag=True 
        break
    l.append(a[1]-a[0])
print(flag)



