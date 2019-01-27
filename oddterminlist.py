y=int(input())
li=[]
for i in range(0,len(str(y))):
  n=y%10
  y=y//10
  if(n%2!=0):
    li.append(n)
print(*li)



