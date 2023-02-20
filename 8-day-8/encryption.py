
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# combine two function in one function


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


should_continie = True
while should_continie:
    direction = input(
        "Type 'encode' for encrypt , Type 'decode' for decrypt : \n").lower()

    text = input("Type your message : \n").lower()

    shift = int(input("Type the shift number : \n"))

    shift = shift % 26

    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input(
        "Type 'yes' for try again and type 'no' for end encryption \n")

    if result == 'no':
        should_continie = False
        print("Bye")


# def encrypt(text_plane, shift_amount):
#     cipher_text = ""
#     for letter in text_plane:
#         position = alphabet.index(letter)

#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):
#     text_plane = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         text_plane += new_letter
#     print(f"The decoded text is {text_plane}")


# if direction == "encode":
#     encrypt(text_plane=text, shift_amount=shift)
# else:
#     decrypt(cipher_text=text, shift_amount=shift)
