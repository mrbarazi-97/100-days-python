import random

my_random_number_int = random.randint(0, 10)

my_random_number_float = random.random()  # between 0 and 1 => [0,1)

# if you want a random float number more than 1 :
# for Exp : [0,5) => you have to * 5

my_random_number_float_new = random.random() * 5  # between 0 and 5 => [0,5)


print(my_random_number_int)
