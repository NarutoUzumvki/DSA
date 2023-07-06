 
def count_element(  list_):
    
    dict_ = {} 
    for ele in list_ :
        if ele not in dict_:
            dict_[ele]=""
            count = 1
        elif ele in dict_:
            count += 1 
            
        else :
            pass
            
        
        print(count)
         
    
    
    return dict_ 


count = 0
list_ = [5, 19, 56, 39, 56 ,19 ,19]


print(list_)
 
sol = count_element(list_)
print(sol)