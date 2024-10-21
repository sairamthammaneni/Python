def largest_and_smallest(a) :
	l=a[0]
	for i in a :
		if l<i :
			l=i
	s=a[0]
	for i in a :
		if s>i :
			s=i
	return l,s
a=[5,3,4,2,1,4,5,32]
Large,Small=largest_and_smallest(a)
print("Largest : ",Large)
print("Smallest : ",Small)
