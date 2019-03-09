u,m=map(int,input().split())
g=list(map(int,input().split()))
r=[]
for i in range(u-m,u):
  r.append(g[i])
print(r)
for i in g:
  if i not in r:
	  r.append(i)
print(*r)
