import random

my_list = ['mohammad', 'ali', 'erfan', 'mohsen', 'omran', 'pooneh']


my_list[-1]  # is pooneh
my_list[2]  # is erfan

my_list[1] = 'naser'  # change item list

my_list.append('reza')  # add item to the end of the list

my_list.extend(['hakan', 'hossein', 'babak'])  # add a list to another list


names = input('please enter list of names just sperate with comma ').split(',')

num_item = len(names)

random_choice = random.randint(0, num_item - 1)
person_who_will_pay = names[random_choice]

print(f'{person_who_will_pay} have to pay today meal')
