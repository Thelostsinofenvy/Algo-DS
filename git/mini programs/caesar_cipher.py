alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(text, shift):
    encrypted_word = ''
    for i in text:
        position = alphabet.index(i) + shift
        if position > 25:
            position -= 26
            encrypted_word += alphabet[position]
        print(encrypted_word)


def decode(text, shift):
    decrypted_word = ''
    for i in text:
        position = alphabet.index(i) - shift
        if position < 0:
            position += 26
            decrypted_word += alphabet[position]
        print(decrypted_word)


if direction == "encode":
    encode(text, shift)
elif direction == "decode":
    decode(text, shift)
