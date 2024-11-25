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