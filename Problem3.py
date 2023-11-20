def cesear_encrypt(input_string, shift_amount):
    result = ""
    for char in input_string:
        if char.isalpha(): #check if the characters are letters
            is_upper = char.isupper() #check for uppercase
            char = char.lower() #Change the uppercase to lowercase
            shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a')) #equation to shift characters (found online)
            if is_upper:
                shifted_char = shifted_char.upper() #Convert letters that were orginally captilized to capital letters
            result += shifted_char
        else:
            result += char #Keep the non-letters unchanged
    return result

def cesear_decrypt(input_string, shift_amount):
    return cesear_encrypt(input_string, -shift_amount)  # Decrypt by encrypting and then using the negative of the shift_amount

#Main methods to call the functions
def main():
    user_input = "Experience is the teacher of all things."
    shift_amount = 12

    encrypted_string = cesear_encrypt(user_input, shift_amount)
    print(encrypted_string)

    decrypted_string = cesear_decrypt(encrypted_string, shift_amount)
    print(decrypted_string)

if __name__ == "__main__":
    main()
