import random
import os


class math:

    def __init__(self, num=0, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
        self.num = num

    def factorial(self, num):
        if num == 0:
            return 0
        if num == 1:
            return 1
        return num * self.factorial(num - 1)

    def factorial2(self):
        if self.num == 0:
            return 0
        if self.num == 1:
            return 1
        return self.num * math(num=self.num - 1).factorial2()

    def isPrime(self):
        for i in range(2, self.num):
            if self.num % i == 0:
                return False
        return True

    def isPrime2(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def commonDivisor(self, num1, num2):
        minimum = min(num1, num2)
        divisors = []
        for i in range(1, minimum):
            if num1 % i == 0 and num2 % i == 0:
                divisors.append(i)
        return divisors


class strings:

    def __init__(self, s1="", s2=""):
        self.s1 = s1
        self.s2 = s2

    def lcs(self, s1, s2):
        longest = []
        temp = ""
        maxx = 0
        lon = ""
        for i in range(0, len(s1)):
            temp = ""
            x = i
            for j in range(i, len(s2)):
                if s1[x] == s2[j]:
                    temp += s1[x]
                    x += 1
            longest.append(temp)
            for i in range(len(longest)):
                if maxx < len(longest[i]):
                    maxx = len(longest[i])
                    lon = longest[i]
        return lon

    def reverseWords(self, s1):
        x = list(reversed(s1.split()))
        reverse = ""
        for i in x:
            reverse += i + " "
        return reverse

    def generate_password(self, length):
        password = ""
        x = 0
        for _ in range(length):
            x = random.randint(31, 126)
            password += chr(x)
        return password

    def unique_words(self, words):
        frequency = {}
        count = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if words[i] == words[j]:
                    count += 1
            frequency.setdefault(words[i], count)
            count = 0
        return frequency


class paths:
    def __init__(self, paths=""):
        self.paths = paths

    def read_from_my_location(self, paths):
        input = open(paths, "r")
        w = input.read().split()
        return w


s = strings()
p = paths()
print("String Class")
print(f"Unique Words from file : {
    s.unique_words(
        p.read_from_my_location(
            r"C:\Users\HP\Desktop\Amit\Advanced_machine_learning_amit\materials\Python_for_ml\workShop\input.txt"
        )
    )}"
)
print(f"longest common subsequence : {
    s.lcs(
        "Welcome To Machine Learning Diploma", "I am Studying a Machine Learning Course"
    )}"
)
print(f"Generated random password : {s.generate_password(10)}")
print(f"Reversed Word : {s.reverseWords("Zeyad Tharwat")}")
print("-" * 50)
print("Math Class")
m = math(3)
print(m.factorial(5))
print(m.factorial2())
print(m.isPrime())
print(m.commonDivisor(20, 40))
