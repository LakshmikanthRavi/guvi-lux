y=int(input())
sum1=0
for i in range(0,len(str(y))):
  d=y%10
  sum1=sum1*10+d
  y=y//10
  z=sum1
  if z==0 or z==1:
    print("yes")
    break
else:
  print("no")
    
