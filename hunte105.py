h=int(input())
k=h%10
sum1=0
for i in range(1,len(str(h))+1):
    g=i**k
    sum1=sum1+g
print(sum1)
