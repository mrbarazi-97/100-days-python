print('Welcome to pizza order system')

size = input('What size pizza do you want ? S , M or L ')
add_pepperoni = input('Do you want pepperoni ? Y or N ')
extra_cheese = input('Do you want extra cheese ? Y or N ')

small_price = 15
medium_price = 20
large_price = 25

price = 0

if size == "S":
    price += small_price
if size == "M":
    price += medium_price
if size == "L":
    price += large_price


if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1


print(f'Dear customer you have to pay ${price}')
