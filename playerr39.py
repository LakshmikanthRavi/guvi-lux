v=int(input())
li=[]
for i in range(1,v+1):
    if 2**i==v:
        print("yes")
        break
else:
    print("no")
