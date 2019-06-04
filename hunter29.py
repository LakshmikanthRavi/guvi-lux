g=int(input())
n=list(map(int,input().split()))
li=[]
for i in range(0,g):
    for j in range(i,g+1):
        li.append(sum(n[i:j]))
g=max(li)
if g==0:
    print(li[1])   
else:
    print(g)
    

