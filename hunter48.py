f=input()
b=input()
p=list(b)
l=list(f)
for i,j in enumerate(f):
  if j==p[0]:
    print(i)
else:
  print(-1)
