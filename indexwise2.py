#Python program to concatenate two lists index wise
l1=["M","na","i","Sai"]
l2=["y","me","s"," Ram","ABC"]
l=[]
for i in range(min(len(l1),len(l2))) :
  ele=l1[i]+l2[i]
  l.append(ele)
i+=1
if(len(l1)==max(len(l1),len(l2))) :
  while i<len(l1) :
    l.append(l1[i])
    i+=1
elif (len(l2)==max(len(l1),len(l2))) :
    while i<len(l2) :
      l.append(l2[i])
      i+=1
print(l)
