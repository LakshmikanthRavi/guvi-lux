u=int(input())
o=list(map(int,input().split()))
li =[]
for i,j in enumerate(o):
  if (((i%2!=0) and (j%2 ==0)) or ((i%2 ==0) and (j%2 !=0))):
    p=j
    li.append(p)
print(*li)
