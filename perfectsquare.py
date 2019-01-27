y,m=map(int,input().split())
g=m*y
for i in range(1,g+1):
  y=i**2
  if(g==y):
    print("yes")
    break
else:
  print("no")
