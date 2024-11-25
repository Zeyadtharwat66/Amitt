# calculator

try:
    options = int(
        input(
            "1-Enter full expression\n2-Enter numbers and choose operation from menu (Max 1 Operation per time)\n"
        )
    )
except Exception:
    print("Unknown choice please Try Again..")
    exit()
if options == 1:
    x = input("Enter your Mathematical Problem : ")
    y = x.replace(" ", "")  # Remove any extra space
    z = ""
    if (
        y.isalpha() and y != "()"
    ):  # Checks that expression does not include any Alphabetic
        print("You Have to Write only numbers and mathematical operators !!")
        exit()
    for (
        i
    ) in y:  # Puts the number in correct format space between each number and operator
        if i.isnumeric() or i == ".":
            z += i
        elif i in "+-*/()":
            z += f" {i} "
        else:
            continue
    operations = z.split()  # split the expression into indexes
    counter = 0
    counter = z.count("+") + z.count("-") + z.count("*") + z.count("/")
    counter += (counter + 1) + z.count(")") + z.count("(")
    if counter != len(
        operations
    ):  # Checks that Count of Operators must be less than count of numbers
        print("Invalid Expression!!")
        exit()
    if (z.__contains__("(") or z.__contains__(")")) and (
        z.count("(") != z.count(")")
    ):  # Check Every bracket has its closure
        print("Ensure the Brackets!!")
        exit()
    try:
        print(eval(z))
    except Exception:
        print("Your Expression has a Math Error")
        exit()
elif options == 2:
    answer = 0
    try:
        x1 = float(input("Enter First Number : "))
        x2 = float(input("Enter Second Number : "))
    except Exception:
        print("You Have to Write only numbers and mathematical operators !!")
        exit()
    operation = int(
        input(
            "Please Choose Operation :\n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n"
        )
    )
    if operation == 1:
        answer = x1+x2
    elif operation == 2:
        answer = x1-x2
    elif operation == 3:
        answer = x1*x2
    elif operation == 4:
        try:
            answer = x1/x2
        except Exception:
            print("Your Expression has a Math Error")
            exit()
    else:
        print("Unknown choice please Try Again..")
    print(answer)
else:
    print("Unknown choice please Try Again..")
