n=input()
l=[]
for i in n:
    if i not in l:
        l.append(i)
x="".join(l)
print(x)
