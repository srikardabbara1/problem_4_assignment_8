def is_divisible(number):
    # Ensure the input is a valid integer
    if not isinstance(number, int):
        return False

    # Convert the number to a string to work with its digits
    number_str = str(number)

    # Initialize the alternating sum to 0
    alternating_sum = 0

    # Iterate through the digits from left to right
    for i, digit in enumerate(number_str):
        # Convert the digit to an integer
        digit_value = int(digit)

        # Alternate between addition and subtraction
        if i % 2 == 0:
            alternating_sum += digit_value
        else:
            alternating_sum -= digit_value

    # Check if the alternating sum is divisible by 11
    return alternating_sum % 11 == 0

# Test the function
number = int(input("Enter a number: "))
if is_divisible(number):
    print("This is divisible by 11.")
else:
    print("This is not divisible by 11.")
