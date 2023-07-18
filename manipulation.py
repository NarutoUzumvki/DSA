
# # def remove_duplicates(para1):
# #     new_dict = {}
# #     elements= sorted(dictionary.items() , key = lambda x:x[1] ,reverse = True)
# #     tuple_elements = tuple(elements)
# #     for  key ,value in tuple_elements:
# #         if (key ,value ) not in new_dict:
# #             new_dict[value] =  new_dict.remove[value] 

# #         else:
# #             pass
# #     return new_dict

# def count_(para):
#     dict_values = dictionary.values
#     new_seq = {}
#     for value in dictionary.values():
#         for element in value:
#             if element not in new_seq:
#                 new_seq[element] = 1 

#             else:
#                 new_seq[element] += 1
#     return new_seq


# # def remove_dup (sol):
# #     for val in sol.values():
# #         if val>1:
# #             sol.pop()

         
         
# #     return sol


# # def sort_list_of_tuples(sol):
# #      sorted_elements = sorted (dictionary.items() , key = lambda x:x[1] , reverse = True )
# #      return sorted_elements

# dictionary = {"Manjeet":[1, 4, 5, 6] , "Akash":[1, 8, 9], "Nikhil":[10, 22, 4], "Akshat":[5, 11, 22]}
# sol = count_(dictionary)
# print(sol)

# ans = remove_dup(sol)
# print(ans)





def get_unique_val(dictionary):
    new_seq = {}
    for value in dictionary.values():
        for elements in value:
            if elements not in new_seq :
                new_seq  [elements] = 1

            else:
                new_seq  [elements] += 1
    return new_seq 



def give_sol(dictionary):

    for key in dictionary:
        temp_list = []
        for value in dictionary[key]:
            
            if unique_value[value] == 1 :
                # print(value) 
                temp_list.append(value)
                # print(val)
           
        dictionary[key] = temp_list

    return dictionary 



 
dictionary = {"Manjeet":[1, 4, 5, 6] , "Akash":[1, 8, 9], "Nikhil":[10, 22, 4], "Akshat":[5, 11, 22]}
unique_value = "The Unique values of keys are {} ."
print(unique_value.format(get_unique_val(dictionary)))

sol = "The Solution is {} ."
print(sol.format(give_sol(dictionary)))





