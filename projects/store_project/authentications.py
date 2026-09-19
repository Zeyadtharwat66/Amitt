from pathlib import Path
import random

ACCOUNTS_FILE = Path(__file__).with_name("Accounts.txt")

class authentications:
    z = {}

    def save_in_file(cls):
        with ACCOUNTS_FILE.open("w", encoding="utf-8") as x:
            x.write(str(cls.z))

    def check_account_from_file(cls):
        with ACCOUNTS_FILE.open("r", encoding="utf-8") as x:
            readable = x.read().replace("{", "").replace("}", "").replace("'", "").split(", ")
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
            return False

    def login(cls, user, password):
        checking = cls.check_account_from_file()
        accounts = {}
        for i in checking:
            mail = i[0 : i.index(":")]
            accounts[mail] = i[i.index(":") + 1 :]
        if user in accounts and password in accounts[user]:
            print(f"Welcome Back {user}")
        else:
            print("Incorrect Data. Try Again")
