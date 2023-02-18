import math
input_height = int(input("please enter height : "))
input_width = int(input("please enter width : "))

coverage_num = 5


def can_calculator(height, width, coverage):
    area = height * width
    cans = math.ceil(area / coverage)
    print(f"You have to buy {cans} cans for your home wall")


can_calculator(height=input_height, width=input_width, coverage=coverage_num)
