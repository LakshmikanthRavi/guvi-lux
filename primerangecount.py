d,j=map(int,input().split())
count=0
for i in range(d,j+1):
  for y in range(2,i):
    if(i%y==0):
      break
  else:
    count=count+1      
print(count)
