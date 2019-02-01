y=int(input())
u=list(map(int,input().split()))
u.sort()
u=u[::-1]
for i in u:
  print(i,end="")


