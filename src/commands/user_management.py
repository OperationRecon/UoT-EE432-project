from services.user_service import authenticate_user


def login():
    name = input("Enter your name: ")
    password = input("Enter Password: ")

    user = authenticate_user(name, password)

    if not user:
        print("Invalid Name or Password")
    else:
        print('Logged in sccuessfully!')
    
    return user
