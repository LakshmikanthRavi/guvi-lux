h,k=map(str,input().split())
p=list(h)
li=[]
o=list(k)
l=[]
for i in range(0,len(h)-1):
    li.append(p[i:i+2])
for j in range(0,len(k)-1):
    l.append(o[j:j+2])
for i in li:
    for j in l:
        if i==j:
            c=1
            break
if c==1:
    print("yes")

else:
    print("no")
