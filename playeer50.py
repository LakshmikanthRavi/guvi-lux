b=int(input())
li=[]
for i in range(2,b):
  if i<b:
    li.append(i)
for i in li:
  if b%i==0:
    print("yes")
    break
else:
  print("no")
