mylist = ["Python", "Javascript", "C++"]
print(type(mylist))

# for x in mylist:
#     print(x)

i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

mylist.sort()
print(mylist)

mylist[2:3] = ["REACT"]
print(mylist)

print(mylist.clear())

