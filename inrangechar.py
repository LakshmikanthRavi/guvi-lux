y=int(input())
r,t=map(int,input().split())
for i in range(r,t):
  if(y==i):
    print("yes")
    break
else:
  print("no")
  
