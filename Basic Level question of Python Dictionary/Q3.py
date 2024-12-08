#Add a new key city to the student dictionary and set its value to "New York".
Student = {"name" :"Ahmad", "Age": 20 , "grade" : "A"}
# Student["city"] = "New york"
Student.update({ "city" : "New York" })
print(Student)