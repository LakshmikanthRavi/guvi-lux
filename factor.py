u=int(input())
y=u
li=[]
for i in range(1,u+1):
  if(y%i==0):
    li.append(i)
print(*li)
