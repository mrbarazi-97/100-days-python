print('welcome to Treasure Island')
print('You have to find treasure in island')

choice1 = input(
    'you\'re at a crossroad , where do you want to go ? "left" or "right" \n ').lower()

if choice1 == 'left':
    # contiue to the game
    choice2 = input(
        'you are in the lake , there is an island in the middle of lake type "wait" to wait and type "swim" to swim \n').lower()
    if choice2 == 'wait':
        choice3 = input(
            'There is a house with 3 doors , one red , one yellow and one blue . which colour do you choose ? \n').lower()

        if choice3 == 'yellow':
            print('You Win')
        else:
            print('Game over')
    else:
        print('Game over')
else:
    print('Game over baby!')
