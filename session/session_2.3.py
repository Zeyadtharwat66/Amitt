x = float(input("Enter your degree : "))
print("Your grade is A") if 100 > x >= 90 else (print("Your grade is B") if 90 > x >= 80 else (print(
    "Your grade is C") if 80 > x >= 70 else (print("Your grade is D")if 70 > x >= 60 else (print("Your grade is F")))))
