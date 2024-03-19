myset = {"Pyhton", "banana", "cherry", "banana", False, 0, 1} #unordered, unchangeable, and unindexed
print(myset)
print(type(myset)) #defined as objects

for x in myset:
    print(x)

myset.add("mangoes") #add new items
print(myset)

myset.remove("banana")
print(myset)

myset.pop()
print(myset)

myset.clear()
print(myset)