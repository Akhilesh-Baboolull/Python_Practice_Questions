
def one_input():
    while True:
        in1 = int(input("Enter the Input(0/1): "))
        if in1 != 0 and in1 != 1:
            print("Invalid Input! Please Re-Enter")
        else:
            break
    return in1


def not_Gate(inp1):
    if inp1 == 1:
        out1 = 0
    else:
        out1 = 1

    return out1

def and_Gate(inp1, inp2):

    if inp1 == 0 or inp2 == 0:
        out1 = 0
    else:
        out1 = 1

    return out1

def or_Gate(inp1, inp2):
    if inp1 == 1 or inp2 == 1:
        out1 = 1
    else:
        out1 = 0

    return out1

def nand_Gate(inp1, inp2):

     if and_Gate(inp1, inp2) == 1:
         out1 = 0
     else:
        out1 = 1

     return out1


def nor_Gate(inp1, inp2):

    if or_Gate(inp1, inp2) == 1:
        out1 = 0
    else:
        out1 = 1

    return out1

def xor_Gate(inp1, inp2):
    if inp1 == inp2:
        out1 = 0
    else:
        out1 = 1

    return out1

while True:
    print("""LOGIC GATES
    Choose 1 for NOT gate
    Choose 2 for AND gate
    Choose 3 for OR gate
    Choose 4 for NAND gate
    Choose 5 for NOR gate
    Choose 6 for XOR gate
    """)

    gate = int(input("Enter Number to choose a Logic Gate: "))

    if gate < 1 or gate > 6:
        print("Invalid choice entered! Please Choose from the above menu")
    else:
        break

if gate == 1:
    print("NOT GATE")

    in1 = one_input()
    output = not_Gate(in1)

elif gate == 2:
    print("AND GATE")

    in1 = one_input()
    in2 = one_input()
    output = and_Gate(in1, in2)

elif gate == 3:
    print("OR GATE")

    in1 = one_input()
    in2 = one_input()
    output = or_Gate(in1, in2)

elif gate == 4:
    print("NAND GATE")

    in1 = one_input()
    in2 = one_input()

    output = nand_Gate(in1, in2)

elif gate == 5:
    print("NOR GATE")

    in1 = one_input()
    in2 = one_input()

    output = nor_Gate(in1, in2)

else:
    print(" XOR GATE")

    in1 = one_input()
    in2 = one_input()

    output = xor_Gate(in1, in2)


print("The Output For Your Selected Gate is :", output )

