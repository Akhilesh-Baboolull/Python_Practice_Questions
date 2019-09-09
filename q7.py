# Initialisation of counts
countvowel = 0
countconso = 0
countdigi = 0
countspchr = 0

sentence = input("Enter Sentence: ")

for character in sentence:

    if character != " ":
        if character.isalpha():
            if character.lower() == "a" or character.lower() == "e" or character.lower() == "i" or character.lower() == "o" or character.lower() == "u":
                countvowel = countvowel + 1
            else:
                countconso = countconso + 1
        elif character.isdigit():
            countdigi = countdigi + 1
        else:
            countspchr = countspchr + 1

print("The Number of Vowels            :", countvowel)
print("The Number of Consonants        :", countconso)
print("The Number of Digits            :", countdigi)
print("The Number of Special Characters:", countspchr)

