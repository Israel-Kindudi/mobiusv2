import random

def generate_unique_six_digit_number(existing_numbers=set()):
    while True:
        number = random.randint(100000, 999999)  # Generate a random six-digit number
        if number not in existing_numbers:  # Check if the number is not already in the existing set
            existing_numbers.add(number)  # Add the number to the set of existing numbers
            return number  # Return the unique six-digit number

# Example usage:
existing_numbers = set()  # Initialize an empty set to store existing numbers
unique_number = generate_unique_six_digit_number(existing_numbers)
print("Unique six-digit number:", unique_number)
