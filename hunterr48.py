f=input()
b=input()
p=list(b)
l=list(f)
if b in f:
  for i,j in enumerate(f):
    if j==p[0]:
      print(i)
      break
else:
  print(-1)
