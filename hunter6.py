n1=int(input())
li=list(map(int,input().split( )))
for i in range(0,len(li)):
    a=li[0]
    li.remove(a)
    if a in li:
        print(a)
        break
    li.append(a)
