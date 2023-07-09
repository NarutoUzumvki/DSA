 
# def count_element(  list_):
    
#     dict_ = {} 
#     for ele in list_ :
#         if ele not in dict_:
#             dict_[ele] = 1 
             
         
            
#         else :
#             dict_[ele] += 1 
            
        
         
#     print (dict_.items())
    
    
#     return dict_ 
#     sorted items = dict.items.sorted(key)


 
# list_ = [5, 19, 56, 39, 56 ,19 ,19]


# print(list_)
 
# sol = count_element(list_)
# print(sol)


 


def count_values(list_):
    dict_ = {}
    for ele in list_ :

        if ele not in dict_:
            dict_[ele] = 1

        else:
            dict_[ele] += 1

    

    return (dict_)


def sort_dict(val):
        my_items = list(val.items())
        my_items.sort()
        sorted = { i,j : val[i],val[j] for i,j in my_items}
        return sorted


 
        


list_ = [ 1, 5 , 99 ,43 ,5 , 1 , 7]

val = count_values(list_)
print(val)

sorted_val = sort_dict(val)
print(sorted_val)


# my_items = list(dict_.items())
# my_items.sort()
# sorted = { i : dict_[i] for i in my_items}
# print(sorted)
 


