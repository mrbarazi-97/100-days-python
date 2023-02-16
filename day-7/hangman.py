import random

word_list = ['mohammad', 'erfan', 'reza', 'majid']


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Test
print(f'the sulotion is {chosen_word}')

# Create blank
display = []
for _ in range(word_length):
    display += "_"
print(display)

guess = input('Please enter a letter : ').lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
