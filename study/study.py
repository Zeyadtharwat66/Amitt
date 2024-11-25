import os

# print(os.getcwd())
# for i in range(20):
#     open(os.path.join(r"C:/Users/HP/Desktop/AMIT/a", f"{i}.txt"), "w")
# x = os.listdir(r"C:/Users/HP/Desktop/AMIT/a")
# for i in x:
#     print(i)

# count = len(x)
# print(count)


# while len(os.listdir(r"C:/Users/HP/Desktop/AMIT/a")) > count/2:
#     z=random.randint(0, 20)
#     print(z)
#     if os.path.exists(fr"C:/Users/HP/Desktop/AMIT/a/{z}.txt"):
#         os.remove(fr"C:/Users/HP/Desktop/AMIT/a/{z}.txt")
# for i in os.walk(r"D:\games"):
#     print(i)
# print(next(os.walk(r"D:\games")))
# def my_generator():
#     yield 1
#     yield 2
#     yield 3


# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

x = [r"C:\HP\Desktop\Amit\Users", r"C:\easy\Desktop\Amit\Users"]

print(os.path.commonpath(x))
