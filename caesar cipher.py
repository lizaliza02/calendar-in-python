
# This function prints greeting for the program.
def welcome():
    ''' WELCOME TO THE CAESAR CIPHER.
This program encrypts and decrypts text with the Caesar Cipher.'''
print(welcome.__doc__)


# This function inputs the data from the user using if else statement.
def enter_message():
    while True:
        user = input("Would you like to encrypt(e) or decrypt(d)?:")
        if user == "e" or user == "d":
            break
        else:
            print("Invalid mode input.")

    while True:
        try:
            choice = input("Would you like to read from a file (f) or the console (c)? ")
            if choice == "f":
                filename = input("Enter a filename:")
                with open(filename, 'r') as input_file:
                    for line in input_file:
                        print(line)
            elif choice == "c":
                break
            else:
                print("Invalid choice.")
        except FileNotFoundError:
            print("INVALID FILENAME: File not found.")

    message = ""
    if user == "e":
        message = input("What message would you like to encrypt: ").upper()
    else:
        message = input("What message would you like to decrypt:").upper()
# This function prompts the user for shift number.
    while True:
        shift = input("What is the shift number(from 1 to 26)?")
        if shift.isdigit():
            shift = int(shift)
            if shift <= 26:
                break
            else:
                print("You can only shift the number from 1 to 26.Please enter again.")

        else:
            print("Invalid shift.")
    return user, message, shift


# This function encrypts the message and shift number.
def encrypt(message, shift_number):
    encrypted_message = ""
    for char in message:
            if char.isalpha():
                shift_c = chr((ord(char) + shift_number - 65) % 26 + 65)
                encrypted_message += shift_c
            else:
                encrypted_message += char
    return encrypted_message


# This function decrypts the code and shift number.
def decrypt(code, shift_number):
    decrypted_text = ""
    for char in code:
        if char.isalpha():
            shift_c =chr((ord(char) - shift_number - 65) % 26 + 65)
            decrypted_text += shift_c
        else:
            decrypted_text += char

    return decrypted_text


# This function finalizes the program.
def main():
    welcome()
    while True:
        user, message, shift = enter_message()
        if user == "e":
            encrypt_message = encrypt(message, shift)
            print(encrypt_message)
        else:
            decrypt_message = decrypt(message, shift)
            print(decrypt_message)
            once_more = input("Would you like to encrypt or decrypt another message?(y/n):")
            if once_more != "y":
                print("Thanks for using the program, Goodbye!")
                break


if __name__=="__main__":
    main()




