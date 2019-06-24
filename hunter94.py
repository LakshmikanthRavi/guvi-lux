h=input()
g=h.split()
li=[]
c=0
for i in g:
    x="".join(reversed(i))
    li.append(x)
    li.append(" ")
li.pop((len(li))-1)
y="".join(li)
print(y)
