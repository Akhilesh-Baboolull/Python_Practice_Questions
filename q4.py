
#print("""   *
#  * *
# *****
#*     *""")


space = " "


while True:
    print("Enter 1 for normal Text")
    print("Enter 2 for Bold Text")
    font = int(input("Enter choice: "))
    if font != 1 and font != 2:
        print("Invalid choice entered! Choose from above menu")
    else:
        break

if font == 1:
    asterisk = "*"
else:
    asterisk = "**"

count = 1

while count <= 4:
    if count == 1:
        print(space + space + space + asterisk)
    elif count == 2:
        print(space + space + asterisk + space + asterisk)
    elif count == 3:
        if font == 1:
            print(space + asterisk + asterisk + asterisk + asterisk + asterisk)
        else:
            print(space + asterisk + asterisk + asterisk + asterisk)
    else:
        print(asterisk + space + space + space + space + space + asterisk)
    count = count + 1

