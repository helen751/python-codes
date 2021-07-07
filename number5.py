print("Assignment using flowcharts on python number 5")
name = (input("What is your name: "))

if name == 'Alice':
    print("Hi alice")

else:
    age = int((input("Enter your age: ")))

    if age < 12:
        print("You are not alice kiddo")

    elif age > 100:
        print("You are not alice grannie")

    # note this statement will never happen because the condition at the top already covers it
    elif age > 2000:
        print("Unlike you alice is not an undead, immortal vampire")
