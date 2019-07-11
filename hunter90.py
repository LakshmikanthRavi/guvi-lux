g=input()
li=[]
for i in g:
    li.append(g.count(i))
p=max(li)
for i in range(0,len(li)):
    if li[i]==p:
        h=i
        break
    

print(g[h],p)
        
