h=int(input())
s=0
for i in range(0,len(str(h))):
    k=h%10
    h=h//10
    k=k**2
    s=s+k
print(s)
