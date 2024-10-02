#Number 12
# enter a string from the user
string = input("Enter a string: ")

# Initialize counters for uppercase and lowercase letters
uppercase_count = 0
lowercase_count = 0

# Iterate through each character in the string
for char in string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

# Print the counts
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)


#Number 13
import re

def check_password(password):
    # Define the criteria
    criteria = [
        (r'[a-z]', "At least 1 letter between [a-z]"),
        (r'[A-Z]', "At least 1 letter between [A-Z]"),
        (r'[0-9]', "At least 1 number between [0-9]"),
        (r'[$%&]', "At least 1 character from [$%&]"),
        (r'.{8,16}', "Length between 8 and 16 characters")
    ]

    # Check each criterion
    errors = [message for pattern, message in criteria if not re.search(pattern, password)]

    # Print feedback
    if errors:
        print("Password is invalid:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Password is valid")

# Accept a password from the user
password = input("Enter a password: ")

# Check the validity of the password
check_password(password)
