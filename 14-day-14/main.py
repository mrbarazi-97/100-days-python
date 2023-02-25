from art import logo, vs
from game_data import data
import os
import random


def clear(): return os.system('clear')


def format_data(account):
    """ Take the account data and return printable format"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name} a {description} , from {country}"


def check_answer(guess, a_flowers, b_flowers):
    """Take the user guess and flower b_flower_countcounts and return if they got it right"""
    if a_flowers > b_flowers:
        return guess == "a"
    else:
        return guess == "b"


# Display logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


# Make the game repeatable
while game_should_continue:
    # Generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # Compare with print
    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")

    guess = input("Who has more flowers ? 'A' or 'B' : ").lower()

    a_flower_count = account_a['follower_count']
    b_flower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_flower_count, b_flower_count)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right, Corrent score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong, final score is {score}")
