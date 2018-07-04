import random

# Generate Phonenumbers by concatenating 7 digits to
# a 562 area code
def generate_phonenumber():
    number = "+1562"
    num = ""
    for x in range(7):
        num = str(random.randint(0, 9))
        number = number + num
    return number


file_names = open("Names.txt", "r")
file_ages = open("Ages.txt", "w")
file_phoneNumbers = open("PhoneNumbers.txt", "w")

for line in file_names:
    file_ages.write(str(random.randint(15, 50)) + "\n")
    file_phoneNumbers.write(generate_phonenumber() + "\n")

file_ages.close()
file_names.close()
file_phoneNumbers.close()
