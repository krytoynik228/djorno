x=5
y=3
spisk=[]
for i in range(x):
  spisk2=[]
  for g in range(y):
    spisk2.append(g*i)
  spisk.append(spisk2)
print(spisk)

for i in range(len(spisk)):
  for g in range(len(spisk[i])):
    if g==len(spisk[i])-1:
      print(spisk[i][g])
    else:
      print(spisk[i][g], end=' ')