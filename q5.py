# Function Definition for operators
def add(n1, n2):  # operator ADDITION
    result = n1 + n2
    return result


def sub(n1, n2):  # operator SUBTRACTION
    result = n1 - n2
    return result


def mul(n1, n2):  # operator MULTIPLICATION
    result = n1 * n2
    return result


def div(n1, n2):  # operator DIVISION
    result = n1 / n2
    return result

# ====================================================================================


operator = ""  # initialisation

while not(operator == "#"):

    while True:
        operator = input("Enter Operator: ")
        if not(operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "#"):
            print("Invalid Operator! Please Re-Enter")  # Validating Operator
        else:
            break

    if not(operator == "#"):
        while True:
            number1 = input("Enter First Number: ")  # User input for first number
            if not(number1.isdigit() or number1 == "#"):
                print("Invalid number entered! Please Re-enter...")
            elif number1.isdigit() or number1 == "#":
                break

        while True:
            number2 = input("Enter Second Number: ")  # User input for second number
            if not (number2.isdigit() or number2 == "#"):
                print("Invalid number entered! Please Re-enter...")
            elif number2.isdigit() or number2 == "#":
                break

        if number1 == "#" or number2 == "#":
            operator = "#"  # This Statement will end the program
        else:
            num1 = int(number1)  # Casting to integer
            num2 = int(number2)  # Casting to integer

    # Executing operator  by calling function
    if operator == "+":
        ans = add(num1, num2)
        print(num1, "+", num2, "=", ans)  # Displaying result
    elif operator == "-":
        ans = sub(num1, num2)
        print(num1, "-", num2, "=", ans)  # Displaying result
    elif operator == "*":
        ans = mul(num1, num2)
        print(num1, "*", num2, "=", ans)  # Displaying result
    elif operator == "/":
        ans = div(num1, num2)
        print(num1, "/", num2, "=", ans)  # Displaying result
    else:
        print("You are Exiting the Program!")  # Message for exiting the program

    print()

