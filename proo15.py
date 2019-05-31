f=int(input())
k=list(map(int,input().split()))
k.sort()
x=k[::-1]
for i in x:
    print(i)
