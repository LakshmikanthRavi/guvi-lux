f=int(input())
t="2"
l=[]
li=[]
c=0
for i in range(1,f+1):
    l.append(i)
for i in l:
    if t in str(i):
        o=list(str(i))
        li.append(o)
for i in li:
    for j in i:
        if j=="2":
            c=c+1
print(c)
        
