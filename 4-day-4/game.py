import random
print('Welcome to my game\n')


rock = ("""Rock
    _______
---'   ____)
      (_____)
      (_____)   
      (____)
---.__(___)
""")

# Paper
paper = ("""Paper
     _______
---'    ____)____
           ______)
          _______)  
         _______)
---.__________)
""")

# Scissors
scissors = ("""Scissors
    _______
---'   ____)____
          ______)
       __________)  
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]


client_choice = int(input(
    'please enter 0 for "Rock" , 1 for "Paper" or 2 for "Scissors" : \n'))
if client_choice >= 3 or client_choice < 0:
    print('You type invalid number , you lose')
else:
    print(game_images[client_choice])

    computer_choice = random.randint(0, 2)
    print(f'Computer choice is : ')
    print(game_images[computer_choice])

    if client_choice == 0 and computer_choice == 2:
        print('You win!')
    elif computer_choice == 0 and client_choice == 2:
        print('You lose')
    elif computer_choice > client_choice:
        print('You lose!')
    elif computer_choice < client_choice:
        print('You win')
    elif computer_choice == client_choice:
        print("It's draw")
