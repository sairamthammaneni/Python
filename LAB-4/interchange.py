# write a program to inter cahnge first and last elements in the list
l=[10,20,30,40,50,60]
print(l)
l[0]=l[0]+l[-1]
l[-1]=l[0]-l[-1]
l[0]=l[0]-l[-1]
print(l)
