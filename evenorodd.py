#Python program to extract even and odd numbers in a list
l=[1,2,3,4,5,6,7,8,9,10]
Even=[]
Odd=[]
for i in l :
  if i%2==0 :
    Even.append(i)
  else :
    Odd.append(i)
print("Even: ",Even)
print("Odd : ",Odd)
