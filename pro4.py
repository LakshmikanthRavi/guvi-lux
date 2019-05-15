f,h=map(str,input().split())
l=[]
i={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
if len(f)==len(h):
  for j in range(0,len(f)):
      g=i[f[j]]-i[h[j]]
      l.append(g)
  print(abs(sum(l)))
elif len(f)>len(h):
  for j in range(0,len(h)):
      g=i[f[j]]-i[h[j]]
      l.append(g)
      o=abs(sum(l))
  for k in range(len(h),len(f)):
    n=abs(sum(l)+i[f[k]])
  print(n)
else:
  for j in range(0,len(f)):
      g=i[f[j]]-i[h[j]]
      l.append(g)
      o=abs(sum(l))
  for k in range(len(f),len(h)):
    n=abs(o+i[h[k]])
  print(n)
