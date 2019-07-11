g=input()
h="".join(reversed(g))
p=[]
for i in h:
    if i not in p:
        p.append(i)
o="".join(p)
print(o)
