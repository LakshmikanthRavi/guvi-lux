g=int(input())
n=list(map(int,input().split()))
li=[]
for i in range(0,len(n)+1):
    li.append(sum(n[0:i]))
g=max(li)
if g==0:
    print(li[1])   
else:
    print(g)
    
