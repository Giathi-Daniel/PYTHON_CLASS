student = {"name" :  "John", 
           "class" : "BCA", 
           "college" : "Turkish-College",
           "student" : True,
           "year" : 2018}
print(type(student)) #ordered, changeable & no duplicates
print(student)

for x in student:
    print(x)

print(len(student))
x = student["name"]
print(x)

y = student.keys() #gives out the keys
print(y)

z = student.values() #gives out the keys
print(z)

student["name"] = "Job" #change dictionary
print(student)

student.clear()
print(student)