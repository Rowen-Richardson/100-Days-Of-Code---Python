#Creating Login Subroutine

print("Welcome to the Login System")



def login():
    count = 0
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    while count < 3:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        if username == "Rowen" and password == "ThisIsMyTestPassword":
            print("Logged in successfully!🥳")
            break
        else:
            print("Incorrect username or password. You have", 3 - count, "attempts left.")
            count += 1
            continue

    if count == 3:
        print("Too many attempts. Please try again later.😢")
        exit()

login()