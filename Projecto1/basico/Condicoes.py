print("Hello Python!")

username = input("Username: ")
password = input("Password: ")

if username == "carlosmacaneta" and password == "macaneta":
    age = int(input("Age: "))
    print("==========================")
    if age >= 18:
        print("you're kid, you'll be kicked off\n2 anos depois...")
    else:
        print("Voce e menor de idade")
else:
    print("Username or password incorrect")