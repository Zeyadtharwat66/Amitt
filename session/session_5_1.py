# # class student:
# #     student_name = "Zeyad tharwat"
# #     __student_age = 22
# #     student_GPA = 3.6
# #     student_Gender = "Male"

# #     def student_info(self):
# #         print(f"Student Name: {self.student_name}")
# #         print(f"Student Age: {self.__student_age}")
# #         print(f"Student GPA: {self.student_GPA}")
# #         print(f"Student Gender: {self.student_Gender}")

# #     def welcomeSt(self):
# #         print(f"hello {self.student_name}")


# # class person:
# #     name = "Zeyad tharwat"
# #     age = 22
# #     Gender = "Male"

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         print("Hello World")

# #     def welcomePr(self):
# #         print("Hello")

# #     def person_info(self):
# #         print(f"Name: {self.name}")
# #         print(f"Age: {self.age}")
# #         print(f"Gender: {self.Gender}")


# # p1 = person("Khaled", 25)
# # p2 = person("Zoz", 18)
# # p1.welcomePr()
# # p1.age = 50
# # print("1 using p1")
# # p1.person_info()
# # print("2 using p1")
# # p2.person_info()
# # person.age = 85
# # print(p1.__dict__)
# # print(p2.__dict__)
# # print(person.__dict__)
# # print("---------------")
# # s1 = student()
# # s1.welcomeSt()
# # s1.__student_age = 80
# # s1.student_info()
# # class person:
# #     name = ""
# #     age = 0
# #     Gender = ""

# #     def __init__(self, name, age, Gender):
# #         self.name = name
# #         self.age = age
# #         self.Gender = Gender


# # class child(person):
# #     father = ""
# #     mother = ""


# #     def __init__(self, father, mother):
# #         self.father = father
# #         self.mother = mother
# class calc1:
#     addition = lambda self, n1, n2: n1 + n2

#     subtraction = lambda self, n1, n2: n1 - n2

#     multiplication = lambda self, n1, n2: n1 * n2

#     def divison(self, n1, n2):
#         return n1 / n2


# class calc2(calc1):
#     power = lambda self, x1, x2: x1**x2


# c1 = calc2()
# print(c1.power(10, 5))

# from abc import ABC, abstractmethod


# class Animal(ABC):
#     name = "animal"

#     @abstractmethod
#     def move(self):
#         pass


# class Dog(Animal):
#     Animal.name = "dog"

#     def move(self):
#         print("Mover from Cat")


# class Cat(Animal):
#     Animal.name = "cat"

#     def move(self):
#         print("Mover from Cat")


# class Bird(Animal):
#     def move(self):
#         print("Mover from Bird")


# # a1 = Animal()
# b1 = Bird()
# # a1.move()
# b1.move()
# print(b1.name)
# # c1 = Cat()
# # c1.move()
# # print(c1.name)


class calc1:
    n1 = 0.0
    n2 = 0.0

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    addition = lambda self: self.n1 + self.n2
    subtraction = lambda self: self.n1 - self.n2
    multiplication = lambda self: self.n1 * self.n2
    division = lambda self: self.n1 * self.n2


print("CALCULATOR")
n1 = float(input("Enter first number : "))
n2 = float(input("Enter second number : "))
c = calc1(n1, n2)
option = int(
    input(
        "Please Choose Operation :\n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n"
    )
)
answer = 0
if option == 1:
    answer = c.addition()
elif option == 2:
    answer = c.subtraction()
elif option == 3:
    answer = c.multiplication()
elif option == 4:
    answer = c.division()
else:
    print("Unknown choice please Try Again..")
print(answer)
