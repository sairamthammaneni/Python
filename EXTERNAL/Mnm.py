l=[] 
n=int(input("Enter the size of list:")) 
print("Enter",n,"number of elements:") 
for i in range (n):
    l.append(int(input())) 
print("The Max position of List is :",l.index(max(l))," and the Min position of List  is :",l.index(min(l)))