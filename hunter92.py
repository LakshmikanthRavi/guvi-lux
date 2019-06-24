h=input()
g=h.split()
li=[]
for i in g:
    for j,k in enumerate(i):
        if j%2==0:
            li.append(k.upper())
        else:
            li.append(k)
            
    li.append(" ")
f=len(li)
li.pop(f-1)
x="".join(li)
print(x)
