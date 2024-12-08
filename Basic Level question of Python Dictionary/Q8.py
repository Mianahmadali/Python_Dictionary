#Iterate through the dictionary student and print all key-value pairs in the format key: value.
Student = {"name" :"Ahmad", "Age": 20 , "grade" : "A", "City" : "New York"}
for keys, values in Student.items():
    print(f"{keys}: {values}")