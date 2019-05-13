b,v=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
print(*l[v-1:v])
