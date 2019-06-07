u,k=map(int,input().split())
y=list(map(str,input().split()))
print(*(y[k:]+y[:k]))
            
