def get_count(characters):
    new_collection = {}
    for value in characters.values():
        for elements in value:
            if elements not in new_collection:
                new_collection[elements] = 1
            else:
                new_collection[elements] += 1

    return new_collection


def remove_duplicate(characters, count_dict):
    for key in characters:
        temp_collection = []
        for value in characters[key]:
            if count_dict[value] == 1 :
                temp_collection.append(value)
        characters[key] = temp_collection

    return characters



def main():
    characters= {"Mugiwara":[1, 4, 5, 6] , "Nami":[1, 8, 9], "Sanji":[10, 22, 4], "Zoro":[5, 11, 22]}

    count_dict = get_count(characters)
    print(count_dict)

    ans = remove_duplicate(characters, count_dict)
    print(ans)

main()


# Immutable Data Type ---> int ,str, tuple 

# Mutable Data Types ---> list, dict, set


