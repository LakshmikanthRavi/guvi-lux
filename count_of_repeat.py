u,v=map(int,input().split())
u=list(map(int,input().split()))
count=0
for i in u:
    if i==v:
      count=count+1
print(count)
