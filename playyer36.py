v,b=map(int,input().split())
s=len(str(v))
c=0
for i in range(0,s):
    n=v%10
    v=v//10
    if n==b:
        c=c+1
print(c)
