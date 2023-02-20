import random
from hangman_art import logo, live_stages
from hangman_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

# rverse stages
reverse_stage = live_stages[::-1]

# number of lives
lives = 6

# Test
print(f'the sulotion is {chosen_word}')

# Create blank
display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input('Please enter a letter : ').lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess} , that's not in word . you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose baby")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print('you win !')

    print(reverse_stage[lives])
