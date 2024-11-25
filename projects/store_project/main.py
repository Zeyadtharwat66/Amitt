from authentications import authentications
from store import store

st = store()
au = authentications()
while True:
    print("-" * 50)
    print("1-SignUp")
    print("2-SignIn")
    x = int(input("choose the option : "))
    if x == 1:
        user = input("Enter your UserName : ")
        password = input("Enter your Password : ")
        au.signup(user, password)
    elif x == 2:
        user1 = input("Enter your UserName : ")
        password1 = input("Enter your Password : ")
        au.login(user1, password1)
        break
    else:
        print("Incorrect Option")
print(st.show_all_products())
while True:
    k = input("Enter The Product You Want To Search For : ")
    print(st.search_products(k))
