
while True:
    num = int(input("Enter a positive number: "))

    if num <= 0:
        print("Wrong number entered! Please Re-enter a positive number...")
    else:
        break

for x in range(0, num + 1, 2):
    print(x)





