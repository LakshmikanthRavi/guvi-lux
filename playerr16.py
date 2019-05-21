p=int(input())
o=list(map(int,input().split()))
o.sort()
li=[]
for i in range(0,p-1):
  if o[i]==o[i+1]:
    if o[i] not in li:
      li.append(o[i])
li.sort()
for i in o:
    if i not in li:
        print(i)
        
        
