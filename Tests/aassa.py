def inscreption(email, user_name, password):
    print("hello user please fill the fallowing instructions")
    a = input("please type your email :")
    b = input("please type your user_name :")
    c = input("please type your password :")

    print(a, b, c)


def loggin():
    print("hello user ")
    user = input("please type your email or user_name :")
    passw = input("please type your password :")


def main():
    global email, user, user_name, password, passw
    print("hello user are you here for [ 1/inscreption or 2/loggin ] ")
    choice = input("what are you want to do : ")

    if choice in ["1", "inscreption"]:
        from fast import inscreption
        print(user_name, email, password)
        while True:
            main()
    elif choice in ["2", "loggin"]:
        loggin()
        if user != email or user != user_name:
            print("your email is incorrect !")
        elif passw != password:
            print("your password is incorrect !")


main()

