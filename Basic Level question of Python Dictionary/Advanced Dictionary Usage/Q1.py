#Merge the following two dictionaries and print the result:
dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4} 
dict1.update(dict2)
print(dict1)


# 2nd method
dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4} 
Mearge = {**dict1,**dict2}
print(Mearge)
