v=int(input())
li=[]
for i in range(1,v+1):
    if v%i==0 and i%2==0:
        li.append(i)
print(*li)
