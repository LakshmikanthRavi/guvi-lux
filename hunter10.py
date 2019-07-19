f,e=map(int,input().split())
k=list(map(int,input().split()))
g=list(map(int,input().split()))
for i in k:
    if i in g:
        print("YES")
        break
else:
    print("NO")
    
