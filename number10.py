print("Assignment using flowcharts on python number 10")

name = ""
while True:
    name = input("Who are you: ")
    while name != 'joe':
        name = input("Who are you: ")

    else:
        password = input("Hello joe what is the password? (it is a fish.): ")
        if password == 'swordfish':
            print("Access Granted")
            break
        else:
            continue

