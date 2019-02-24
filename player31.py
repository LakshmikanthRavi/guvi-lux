u=input()
y=list(u)
c=0
b=0
for i in y:
  if i==("("):
    c=c+1
  elif i==(")"):
    b=b+1
if(c==b):
  print("yes")
else:
  print("no")
