u=int(input())
li=[]
for i in range(0,u+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            li.append(i)
print(*li)
