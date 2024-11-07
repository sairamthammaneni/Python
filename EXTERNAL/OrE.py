l=[] 
n=int(input("Enter the No.of Element: ")) 
for i in range(n): 
 ele=int(input("Enter the element:")) 
 l.append(ele) 
print(l) 
even=[] 
odd=[] 
for i in range(len(l)): 
 if(l[i]%2==0): 
  even.append(l[i]) 
 else: 
  odd.append(l[i])  
print(even) 
print(odd) 