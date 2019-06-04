n=input()
l=list(n)
l.sort()
li=[]
for i in range(0,len(n)-1):
    if(l[i]==l[i+1]):
        if l[i] not in li:
            li.append(l[i])
li.sort()
x="".join(li)
print(x)
