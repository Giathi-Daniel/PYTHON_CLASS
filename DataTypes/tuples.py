mytuple = ("Javascript", "Python", "React", "React", 1, True) #store multiple items in a single variable
print(type(mytuple)) #ordered, unchangleable, allow duplicates
print(mytuple)
print(len(mytuple))
print(mytuple[3])
print(mytuple)

# loop the whole tuple
for x in mytuple:
    print(x)

# # loop through index
for i in range(len(mytuple)):
    print(mytuple[i])
