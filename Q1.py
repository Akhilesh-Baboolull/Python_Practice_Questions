while True:
    while True:
        char = input("Enter a character: ")
        if not(len(char) == 1):
            print("You Need To Enter Only One Character! Please Re-Enter")
        else:
            break

    if char.isalpha():
        if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
            print(char + " is a vowel.")

        else:
            print(char + " is a consonant")

# elif char.isdigit():
#    print(char + " is a digit")

# else:
#    print(char + " is a special character.")

    while True:
        print("Enter 1 to Re-Try program")
        print("Enter 2 to exit")

        choice = int(input("Enter choice: "))

        if not(choice == 1 or choice == 2):
            print("Invalid choice entered! Please Re-Enter")
        else:
            print("You are Exiting the Program!")
            break

    if choice == 2:
        break
    else:
        print()
