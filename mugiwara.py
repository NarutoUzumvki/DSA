def get_count(collection):
    new_collection = {}
    for value in collection.values():
        for element in value:
            if element not in new_collection:
                new_collection[element] = 1
            else:
                new_collection[element]  += 1

    return new_collection

def remove_redundant_value(collection, element_count ):
    for key in collection:
        temp_collection = []
        for value in collection[key]:
            if element_count[value] == 1 :
                temp_collection.append(value)

            collection[key] = temp_collection

    return collection






def main():
    
    collection = {" monkey.d.luffy " : [2, 5, 7, 12] , " mugiwaraa " : [2, 19,7] , " luffy " : [2,18]}

    element_count = get_count(collection) 
    print(" The element count of values in collection are : ")
    print(element_count)

    unique_values_collection = " The unique value of collection are : {} ."
    print(unique_values_collection.format(remove_redundant_value(collection, element_count )))

main()