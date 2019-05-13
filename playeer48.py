b=int(input())
li=[]
l=[]
if b%2==0:
  for i in range(1,b):
   if b%i==0:
     li.append(i)
  for i in li:
   if i%2!=0:
     l.append(i)
  print(*l)
elif b%2!=0:
  for i in range(1,b):
   if b%i==0:
     li.append(i)
  for i in li: 
   if i%2!=0:
     l.append(i)
  if b in l:
    print(*l)
  else:
    l.append(b)
    print(*l)


