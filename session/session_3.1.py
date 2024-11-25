def fun(name, age=20):
    print(f"My name is {name},My age is {age}")


def fun2(*name):
    print(name)
    print(type(name))


def sum(*x):
    summ = 0
    for i in x:
        summ += i
    return summ


# x = []
# while True:
#     y = int(input("Enter numbers : "))
#     x.append(y)
#     if y == 0:
#         break
# z = tuple(x)
# print(sum(*z))
fun3 = lambda x, y: x + y
print(fun3)
print(type(fun3))
fun("Zeyad")
fun2("Zeyad", "Khaled", 15, 80, True, 8.6)
