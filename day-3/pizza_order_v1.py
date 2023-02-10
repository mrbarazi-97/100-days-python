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
    if add_pepperoni == "Y":
        price += 2
    if extra_cheese == "Y":
        price += 1
elif size == "M":
    price += medium_price
    if add_pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
elif size == "L":
    price += large_price
    if add_pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1
    print(f'Dear customer you have to pay ${price}')
else:
    print('Try again')
