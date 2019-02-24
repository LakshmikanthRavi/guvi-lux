n1=int(input())
li=list(map(int,input().split( )))
c=k=0
for i in range(0,len(li)):
    if i%2==0:
        c=c+li[i]
    else:
        k=k+li[i]
if c>k:
    print(c)
else:
    print(k)
        
