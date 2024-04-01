mylist = ["Python", "Javascript", "C++", "Python"] #ordered, changeable and allow duplicate
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


#add all items in a list
def sum_total(items):
    sum_numbers = 0
    multiply_numbers = 0

    for x in items:
        sum_numbers += x
        multiply_numbers *= x

    return sum_numbers, multiply_numbers
    
print(sum_total([20,23,-30]))
print(sum_total([20,23,-30]))

