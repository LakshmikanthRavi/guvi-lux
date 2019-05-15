g,h=map(str,input().split())
li=[]
count=0
for i in g:
  li.append(i)
for i,j in enumerate(li):
  if j==h:
    count=count+1
print(count)
 
