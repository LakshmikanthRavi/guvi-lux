a,m=map(int,input().split())
for i in range(0,a):
  y=m**i
  if y==a:
    print("yes")
    break
else:
  print("no")
 
