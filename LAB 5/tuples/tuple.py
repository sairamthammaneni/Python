t1=(1,2,3,4)
t2=('a','b','c','d')
print(t1)
print(t2)
print(t1+t2) #concate
print(t1*3) #repeatation
print(t1[1]) #index
print('a' in t2) #membership(boolean)
for i in t1 :
	print(i) #iterations
t3=t1+t2+(1,2,1,4,1,3)
print(t3) #assigning
#slicing
print(t3[::-1])
print(t3[:2])
#Methods in tuple
print(t3.index('a')) #index
print(len(t3)) #len
print(t3.count(1)) #count
print(tuple(zip(t1,t2)))
