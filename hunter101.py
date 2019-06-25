u=int(input())
li=[]
l=[]
for i in range(0,u):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            li.append(i)
for i in li:
    for j in li:
        for k in li:
            f=i+j+k
            if f==u:
                l.append([i,j,k])
print(*l[0])
        
        
