def s(my_list): 
    x=max(my_list) 
    my_list.remove(x) 
    return max(my_list) 
l=[1,2,3,4] 
print(s(l)) 