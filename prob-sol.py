# Find unique elements from a list. Answer can be in random order.
 

def unique_element(list_):
    set_ = set()
    for ele in list_ :
        set_.add(ele)
    return set_


list_ = [23 ,'Halloween' ,"Gamora" ,59 ,63 , 'Halloween' ,63]

 
 
    
 
print(unique_element(list_))
    
    
 

