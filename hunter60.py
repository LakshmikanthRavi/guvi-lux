u=int(input())
y=list(map(str,input().split()))
g=list(map(str,input().split()))
for i in range(0,u):
    if y[i:]+y[:i]==g:
        z=i
print(z)    
