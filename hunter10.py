f,e=map(int,input().split())
k=list(map(int,input().split()))
g=list(map(int,input().split()))
if len(g)<len(k):
    for i in g:
        if i in k:
            print("YES")
            break
    else:
        print("NO")
else:
    print("NO")
    
