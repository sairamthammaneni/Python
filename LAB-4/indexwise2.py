#Python program to concatenate two lists index wise
l1=["M","na","i","Sai"]
l2=["y","me","s"," Ram","ABC"]
l=[]
for i in range(min(len(l1),len(l2))) :
  ele=l1[i]+l2[i]
  l.append(ele)
print(l)
