y=input().split(" ")
li=[]
for i in y:
  s="".join(reversed(i))
  li.append(s)
print(*li)

