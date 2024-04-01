# def f():
#     s = "I love programming" #Local variable
#     print(s)


# s = "Me too" #global variable
# f()
# print(s)


# def f():
#     global s
#     print(s)
#     s = "I love programming" # modified global variable
#     print(s)

# s = "Python is great"
# f()
# print(s)

x = 50
def fun1():
    x = 25
    print(x)
fun1()
print(x)


def func1():
    x = 50
    return x
func1()
print(x)
