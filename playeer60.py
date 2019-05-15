f,k=map(str,input().split())
c=0
for i in f:
    for j in k:
        if i in j:
            c=1
    break
if(c==1):
    print("yes")
else:
    print("no")
