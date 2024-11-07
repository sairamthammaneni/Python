l=[] 
n=int(input("Enter no.of Elements : ")) 
for i in range(n): 
    ele=int(input("Enter elements : ")) 
    l.append(ele) 
print(l) 
print("Sum of list is : ",sum(l)) 
print("Average of list is : ",sum(l)/len(l)) 