u=int(input())
o=input()
l=[]
for i in o:
  if i=="a" or i=="A" or i=="e" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
    continue
  l.append(i)
s="".join(reversed(l))
print(s)
  

  
