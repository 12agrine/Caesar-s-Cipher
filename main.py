from alphabet import alphabet
from art import logo
print(logo)


def caesar(start_text, shift_amount, cipher_direction):
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
    print(f"The {cipher_direction}d message is {end_text}.")


should_continue = True

while should_continue:
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    start_text = input("Type in your message.\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    shift_amount = shift_amount % 26
    caesar(start_text, shift_amount, cipher_direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
