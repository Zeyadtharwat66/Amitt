def zero(op=None): return 0 if op is None else op(0)
def one(op=None): return 1 if op is None else op(1)
def two(op=None): return 2 if op is None else op(2)
def three(op=None): return 3 if op is None else op(3)
def four(op=None): return 4 if op is None else op(4)
def five(op=None): return 5 if op is None else op(5)
def six(op=None): return 6 if op is None else op(6)
def seven(op=None): return 7 if op is None else op(7)
def eight(op=None): return 8 if op is None else op(8)
def nine(op=None): return 9 if op is None else op(9)

# Arithmetic operations
def plus(num):
    return lambda x: x + num

def minus(num):
    return lambda x: x - num

def times(num):
    return lambda x: x * num

def divided_by(num):
    return lambda x: x // num 

print(seven(times(four())))