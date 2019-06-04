import numpy
g=int(input())
n=list(map(int,input().split()))
li=[]
for i in range(0,g):
    for j in range(i,g+1):
        l=numpy.prod(n[i:j])
        li.append(l)
g=(int(max(li)))
if g==0:
    print(int(li[1]))   
else:
    print(g)
    
