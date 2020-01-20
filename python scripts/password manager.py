import random

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890' \
        '!@#$%^&*()\[]{}";:/?.>,<`~-_=+'
length = input("How long do you want your password to be?")
length = int(length)
numpasswords = input("How many passwords would you like to create?")
numpasswords = int(numpasswords)

for numberOfPasswords in range(numpasswords):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
