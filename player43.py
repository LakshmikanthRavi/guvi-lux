a,b=map(str,input().split())
li=[]
l=[]
for i in a:
    li.append(i)
for j in b:
    l.append(j)
if i in j:
    print("yes")
else:
    print("no")
