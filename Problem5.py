"""
Assumptions:
1. The cipher is a legit sentence
2. The correct decryption is the one that has the most common words in it.

Logic:
I used the Brute Force Technique which I found online as a common way to decipher Cesears Cryptic.
Essentially I tried the encrpyted message with shift keys of 1-26, all possible values and stored each possibility as best message until a new one with more common words was added.
I then took the list with the most amount of common words in it and printed that out using assumption 2.
"""

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            common_words = set(line.strip().lower() for line in file if line.strip()) #clean, strip and lowercase
            return common_words
    except FileNotFoundError:
        print("Common words file not found.")
        return set()

def caesar_brute_force(ciphertext, common_words):
    best_shift = None
    best_message = None
    best_common_word_count = 0

    for shift in range(1, 27):  # Try all possible shift values
        decrypted_message = ""
        common_word_count = 0
        #pulled this code straight from problem 3
        for char in ciphertext:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                if is_upper:
                    shifted_char = shifted_char.upper()
                decrypted_message += shifted_char
            elif char.isspace():
                decrypted_message += ' '

        words = decrypted_message.split()
        #loop through each word in words and add to common word count if it is in the common words list
        for word in words:
            if word.lower() in common_words:
                common_word_count += 1
        #Compares the newest key shift to the current highest common word count and replaces if this one is greater
        if common_word_count > best_common_word_count:
            best_shift = shift
            best_message = decrypted_message
            best_common_word_count = common_word_count

    return best_shift, best_message, best_common_word_count

# Load the list of common words
common_words = process_file("/Users/srikardabbara/Documents/common_words.txt")

# The ciphertext you want to decrypt
ciphertext = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"

# Perform the Caesar cipher brute force decryption and select the best result
best_shift, best_message, best_common_word_count = caesar_brute_force(ciphertext, common_words)

# Print the best result
print(f"Best Shift: {best_shift}")
print(f"Decrypted Message: {best_message}")

