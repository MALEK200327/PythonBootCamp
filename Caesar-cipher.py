alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#encrypting
if direction == "encode" :

    def encrypt(text, shift):
        newWord=""
        for letters in text:
            if letters in alphabet:
                position = alphabet.index(letters)
                new_position = position + shift
                newWord+=alphabet[new_position]
        print(newWord)
    encrypt(text,shift)

else:
    def decrypt(text,shift):
        newWord=""
        for letters in text:
            if letters in alphabet:
                position = alphabet.index(letters)
                new_position = position - shift
                newWord+=alphabet[new_position]
        print(newWord)
    decrypt(text,shift)

