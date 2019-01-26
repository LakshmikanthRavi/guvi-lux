u=int(input())
y=u
for i in range(2,u):
  if(y%i==0):
    print("yes")
    break
else:
  print("no")
