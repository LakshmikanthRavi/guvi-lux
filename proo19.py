p=int(input())
li1=[]
for i in range(p):
    
    li=list(map(int,input().split( )))
    for i in li:
        li1.append(i)
li1.sort()
print(*li1)
