# def unique_elements(lst):
 #     # global dict_  
 #     dict_ = {}

#     for elements in lst:
#         if elements not in dict_:
#             dict_[elements] = 1

#         else:
#             dict_[elements] += 1

#     # global kv_in_tuples

#     # kv_in_tuples = dict_.items()

#     return dict_

# def sort_dict(dict_):
#     sorted_element = sorted(dict_.items(), key=lambda x:x[1] ,reverse = True)
#     # convert_to_dict = dict(sort_)
#     # return convert_to_dict
#     return sorted_dict


# lst = [50 ,302 ,100 ,205 ,302 ,100 ,"kill me" ,"trapped in my damn mind!"]


# sorted_element = sort_dict(dict_)
# print(sorted_dict_(dict_))


# **************************************************************************************
 


# def get_unique_elements(list_seq):
    
#     for element in list_seq:
#         if element not in dict_seq:
#             dict_seq[element] = 1

#         else:
#             dict_seq[element] += 1

#     return dict_seq


# def sort_seq(get_unique_elements):
#     sorted_elements = sorted(dict_seq.items() , key = lambda x:x[1] , reverse = True)
#     return sorted_elements


# # def convert_to_dict (sort_seq):
# #     for key,values in dict_seq.items():
# #         converted = dict_seq.items().sort
# #     return converted

# def print_sorted_elements(get_unique_elements ,sort_seq ):

#     sol = get_unique_elements (list_seq)
#     print(sol)

#     sorted_sol = sort_seq(get_unique_elements)
#     print(sorted_sol)
    






# list_seq = [ 10, 15, 11, "anyways", 23, 10, 55, "anyways", 46, 23, "something or the other"]

# dict_seq = {}


# print_sorted_elements( get_unique_elements ,sort_seq)
 

# for a,b in :
#     print(a,b)








def unique_elements ( lst_seq ):
    dict_seq = {}
    for element in lst_seq :
        if element not in dict_seq:
            dict_seq[element] = 1 

        else:
            dict_seq[element] += 1
    return dict_seq



def sort_elements(uniq_elemnts):
    sorted_elements = sorted (uniq_elemnts.items() , key = lambda x:x[1] , reverse = True )
    return sorted_elements

def print_sorted_elements(sorted_seq):
    for x in sorted_seq:
        print(x)


def convert_to_dict(list_of_tuples):
    new_dict = {}

    for key, value in list_of_tuples:  # unpacking of tuple
        new_dict[ key ] = value

    return new_dict

def main():
    lst_seq = [ 10 ,15 ,302 ,111 ,"hello" ,"world" ,10 ,15 ,15 ,"hello" , "hello"]

    uniq_elemnts = unique_elements(lst_seq)
    print(uniq_elemnts)

    sorted_seq = sort_elements (uniq_elemnts)
    print(sorted_seq)
 
    print_sorted_elements(sorted_seq)

    new_dict_elements = convert_to_dict(sorted_seq)
    print(new_dict_elements)

print(__name__)

if __name__ == "__main__" :
    main()






