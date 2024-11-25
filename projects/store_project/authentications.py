import random


class authentications:
    z = {}

    def save_in_file(cls):
        x = open(
            r"C:\Users\HP\Desktop\Amit\Advanced_machine_learning_amit\materials\Python_for_ml\projects\store_project\Accounts.txt",
            "w",
        )
        x.write(str(cls.z))

    def check_account_from_file(cls):
        x = open(
            r"C:\Users\HP\Desktop\Amit\Advanced_machine_learning_amit\materials\Python_for_ml\projects\store_project\Accounts.txt",
            "r",
        )
        readable = (
            x.read().replace("{", "").replace("}", "").replace("'", "").split(", ")
        )
        return readable

    def signup(cls, user, password):
        cls.z.setdefault(user, password)
        cls.save_in_file()
        if cls.verification_code() == True:
            print(f"Welcome {user}")
        else:
            print("Incorrect Verification Code. Try Again")

    def verification_code(cls):
        ver = random.randrange(10000, 1000000)
        print(f"Your verification Code is {ver}")
        while True:
            check = int(input("Enter the Verification Code : "))
            if check == ver:
                return True
            else:
                return False

    def login(cls, user, password):
        checking = cls.check_account_from_file()
        accounts = {}
        for i in checking:
            mail = i[0 : i.index(":")]
            accounts[mail] = i[i.index(":") + 1 :]
        if user in accounts:
            if password in accounts[user]:
                print(f"Welcome Back {user}")
            else:
                print("Incorrect Data. Try Again")
        else:
            print("Incorrect Data. Try Again")
