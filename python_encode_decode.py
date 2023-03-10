import base64

def encode(key, message):
    """Encode message"""

    encoded = []

    """The remainder of division between i and len(key) uses the remainder 
    as index of key, value of key at index is stored in key_chars.

    The function ord() is used to get integer unicode value of unicode character (message), 
    then convert the value at index i into integer value. The remainder of division
    of addition of ord(message[i]) and ord(key_chars) with 256 is converted then stored in encoded.
    
    encode() returns a utf-8 encoded message, decode() will decode the string"""

    for i in range(len(message)):
        key_chars = key[i % len(key)]
        encoded.append(chr((ord(message[i]) + ord(key_chars)) % 256))

    return base64.urlsafe_b64encode("".join(encoded).encode()).decode()


def decode(key, message):
    """Decode message"""

    decoded = []
    message = base64.urlsafe_b64decode(message).decode()

    """The remainder of addition of 256 with the subtraction and the division with 256
    will give a remainder that is then passed in the chr function to convert the integer
    value to string and store to decoded"""

    for i in range(len(message)):
        key_chars = key[i % len(key)]
        decoded.append(chr((256 + ord(message[i]) - ord(key_chars)) % 256))

    return "".join(decoded)


def mode(choice):
    """Set mode"""

    if choice.lower() == 'e' or choice.lower() == 'encode':
        text,private_key = get_message_and_pk()
        result = encode(private_key, text)
        print(f'\nEncoded message: {result}')
    elif choice.lower() == 'd' or choice.lower() == 'decode':
        private_key,encryption_message=get_encrypted_message()
        result = decode(private_key, encryption_message)
        print(f'\nDecoded message: {result}')
    else:
        print('\nInvalid Mode!\n')

def get_message_and_pk():
    text = input('Enter a message: ')
    private_key = input('Enter a private key to use: ')
    return text,private_key

def get_encrypted_message():
    private_key = input('Enter a private key: ')
    encryption_message = input("Input encyption message")    
    return private_key,encryption_message

def main():

    choice = input('Mode (Encode or Decode): ')
    mode(choice)


if __name__ == '__main__':
    main()
