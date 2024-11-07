l1=["M","na","i","Abhi"] 
l2=["y","me","s","Ram"] 
l=[] 
print(list(zip(l1,l2))) 
for i in range (len(l1)) : 
 l.append(l1[i]+l2[i]) 
print(l)