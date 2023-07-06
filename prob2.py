class Dictionary:

    def count(self ,dict_):
        for ele in list_ :
            dict_[ele] = "" 
             
        return dict_ 




list_ = ["pundri" , "sundri" ,56 ,39 ,56]
dict_ = {}

print(list_)
obj = Dictionary()

print(obj.count(dict_))