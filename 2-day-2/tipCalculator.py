print('Hi and welcome to Baraz tip calculator')

bill = float(input('Please enter the total bill : '))
tip = int(input('How much tip would you like to give ? 10 , 12 , or 15 ? '))
num_of_people = int(input('How many people to split the bill ? '))

bill_calculate = round( bill * (1+(tip/100)) / num_of_people , 3)


print(f'Each person should pay : ${bill_calculate}')