p=int(input())
o=list(map(int,input().split()))
li=[]
for i in range(p-1):
  if o[i]==o[i+1]:
    li.append(o[i])
if len(li)!=0:
  print(*li)
elif len(li)==0:
  print("unique")
  
