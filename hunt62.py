d=int(input())
h=list(map(int,input().split()))
h.sort()
f=h[0]
j=max(h)
k=j-f
print(k)
