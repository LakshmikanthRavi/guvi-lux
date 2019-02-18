y=int(input())
li=[]
t=0
l=0
for i in range(len(str(y))):
  c=y%10
  t=t+c
  y=y//10
g=t
if(len(str(g))==1):
  print("YES")
else:
  for i in range(len(str(g))):
    f=g%10
    l=l*10+f
    g=g//10
    if l==g:
      print("YES")
      break
  else:
    print("NO")

  

  

