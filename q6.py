
password = input("Enter Password: ")

encryptedpass = ""
for x in password:
    encval = (ord(x) % 128) + 2
    encryptedpass = encryptedpass + chr(encval)

print("Tne Encrypted Password is:", encryptedpass)




