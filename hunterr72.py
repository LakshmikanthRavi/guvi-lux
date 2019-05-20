w=input().split()
y=list(w)
li=[]
for i,j in enumerate(y):
    if (i+1)%2==0:
        li.append(j)
    if (i+1)%2!=0:
        d="".join(reversed(j))
        li.append(d)
print(*li)
        
