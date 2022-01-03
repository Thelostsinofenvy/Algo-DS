alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode(text, shift):
    encrypted_word = ''
    for i in text:
        if i not in alphabet:
            encrypted_word = encrypted_word + i
            continue
        position = alphabet.index(i) + shift
        if position > 25:
            position -= 26
            encrypted_word += alphabet[position]
        else:
            encrypted_word += alphabet[position]
    print(encrypted_word)


def decode(text, shift):
    decrypted_word = ''
    for i in text:
        if i not in alphabet:
            decrypted_word = decrypted_word + i
            continue
        position = alphabet.index(i) - shift
        if position < 0:
            position += 26
            decrypted_word += alphabet[position]
        else:
            decrypted_word += alphabet[position]
    print(decrypted_word)


online = True
while online == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encode(text, shift)
    elif direction == "decode":
        decode(text, shift)
    print("type 'yes' to go again or type 'no' to quit! ")
    ans = input()
    if ans.lower() == 'no':
        online = False
        print("goodbye")
