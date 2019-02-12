p=int(input())
o=list(map(int,input().split()))
o.sort()
li=[]
for i in range(0,p-1):
  if o[i]==o[i+1]:
    if o[i] not in li:
      li.append(o[i])
li.sort()
if len(li)!=0:
  print(*li)
elif len(li)==0:
  print("unique")
  
