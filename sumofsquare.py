n=int(input())
sum1=0
while(n>0):
  y=n%10
  v=y**2
  sum1=sum1+v
  n=n//10
print(sum1)
