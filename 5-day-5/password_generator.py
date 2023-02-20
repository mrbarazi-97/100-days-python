import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print('Welcome to my pasword generator app')

nr_letter = int(input('How many letter do you want ? \n'))
nr_number = int(input('How many number do you want ? \n'))
nr_symbol = int(input('How many symbol do you want ? \n'))

# Not hard
password = ""

for char in range(1, nr_letter + 1):
    password += random.choice(letters)

for char in range(1, nr_number + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbol + 1):
    password += random.choice(symbols)


print(f'Your password is here : {password}')


# Hard

password_list = []

for char in range(1, nr_letter + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_number + 1):
    password_list += random.choice(numbers)

for char in range(1, nr_symbol + 1):
    password_list += random.choice(symbols)


print(f'Your password is here : {password_list}')
random.shuffle(password_list)
print(f'Your password is here : {password_list}')


password = ""

for char in password_list:
    password += char

print(f'Your final password is here : {password}')
