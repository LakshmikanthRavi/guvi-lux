v=input()
li=[]
for i in v:
  if i==i.upper():
    y=i.lower()
    li.append(y)
  elif i==i.lower():
    h=i.upper()
    li.append(h)
p="".join(li)
print(p)
