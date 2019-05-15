s=int(input())
s1=list(map(int,input().split()))
li=[]
l=[]
for i in range(0,s-1):
    if s1[i]>=s1[i+1]:
        li.append(s1[i])
for i in li:
    if i>0:
        l.append(i)
print(*l)

