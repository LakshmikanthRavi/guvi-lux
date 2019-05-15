c,k=map(int,input().split())
s=list(map(int,input().split()))
for i in range(0,c-1):
    for j in range(i+1,c):
        if(s[i]+s[j]==k):
            c=1
            break
if(c==1):
    print("yes")
else:
    print("no")
