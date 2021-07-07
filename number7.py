print("Assignment using flowcharts on python number 7")
ask1 = input("Is it raining: ")
if ask1 == 'yes':
    ask2 = input("Do you have an umbrella: ")
    if ask2 == 'no':
        print("Wait a while")

        ask3 = input("Is it raining: ")
        while ask3 == 'yes':
            print("wait a while")
            ask3 = input("Is it raining: ")


print("Go outside")
