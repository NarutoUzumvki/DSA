def unique_elements(lst):
    global dict_  
    dict_ = {}

    for elements in lst:
        if elements not in dict_:
            dict_[elements] = 1

        else:
            dict_[elements] += 1

    global kv_in_tuples

    kv_in_tuples = dict_.items()

    return dict_

def sorted_dict_(dict_):
    sort_ = sorted(dict_.items(), key=lambda x:x[1])
    convert_to_dict = dict(sort_)
    return convert_to_dict


lst = [50 ,302 ,100 ,205 ,302 ,100 ,"kill me" ,"trapped in my damn mind!"]

print(unique_elements(lst))
print(sorted_dict_(dict_))








