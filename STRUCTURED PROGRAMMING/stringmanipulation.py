#number 2
# Define the input string
string_input= "programming"

# Initialize an empty dictionary to store character counts
character_count = {}

# Iterate through each character in the string
for character in string_input:
    # Increment the count for each character
    if character in character_count:
        character_count[character] += 1
    else:
        character_count[character] = 1

# Print the character counts
for character, count in character_count.items():
    print(f"Character '{character}' occurs {count} times")
    
    
#number 4
# Input strings
str1 = "abc"
str2 = "xyz"
def concatenate_and_swap(str1, str2):
    # Concatenate the two strings
    concatenated_str1 = str2[:2] + str1[2:]
    concatenated_str2 = str1[:2] + str2[2:]
    
    # Swap the first two characters
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]
    
    return swapped_str1, swapped_str2



# Concatenate and swap first two characters
result1, result2 = concatenate_and_swap(str1, str2)

# Print the results
print(f"After concatenating and swapping first two characters:")
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")

#number7

# Input string
input_string = "computer science"

def remove_odd_indices(input_string):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the string and add characters at even indices to result
    for index in range(len(input_string)):
        if index % 2 == 0:
            result += input_string[index]

    return result


# Remove characters at odd indices
result_string = remove_odd_indices(input_string)

# Print the result
print(f"After removing characters at odd indices: {result_string}")


#number 6
# Input string
input_string = "python"

def swap_first_last(input_string):
    if len(input_string) < 2:
        return input_string
    
    first_character = input_string[0]
    last_character = input_string[-1]
    middle_characters = input_string[1:-1]
    
    # Swap first and last characters and concatenate
    swapped_string = last_character + middle_characters + first_character
    
    return swapped_string


# Swap first and last characters
result_string = swap_first_last(input_string)

# Print the result
print(f"After swapping first and last characters: {result_string}")

#number 9
# Input string
input_string = "Hello World"

def convert_case(input_string):
    # Convert to uppercase
    uppercase_string = input_string.upper()
    
    # Convert to lowercase
    lowercase_string = input_string.lower()
    
    return uppercase_string, lowercase_string

#NUMBER 10
# Input string
input_string = "python"
def reverse_string(input_string):
    # Using slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string

# Reverse the string
reversed_result = reverse_string(input_string)

# Print the result
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_result}")



# Convert to uppercase and lowercase
uppercase_result, lowercase_result = convert_case(input_string)

# Print the results
print(f"Original String: {input_string}")
print(f"Uppercase String: {uppercase_result}")
print(f"Lowercase String: {lowercase_result}")


#NUMBER 12

string = "Hello World"

def reverse_words(string):
    # Split the input string into words
    words = string.split()

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join the reversed words into a single string
    reversed_string = " ".join(reversed_words)

    return reversed_string


# Reverse the words in the string
reversed_result = reverse_words(string)

# Print the result
print(f"Original String: {string}")
print(f"Reversed Words String: {reversed_result}")


#NUMBER16
def sum_of_digits(input_string):
    # Initialize sum to zero
    total_sum = 0

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            # Convert the character to an integer and add to total_sum
            total_sum += int(char)
    
    return total_sum

# Input string
input_string = "Hello 1234"

# Compute the sum of digits
sum_digits = sum_of_digits(input_string)

# Print the result
print(f"Input String: {input_string}")
print(f"Sum of Digits: {sum_digits}")

#NUMBER 18

def count_characters(string):
  """
  This function counts the occurrences of uppercase letters, lowercase letters,
  digits, and special characters in a given string.

  Args:
      string: The string to analyze.

  Returns:
      A dictionary containing counts for uppercase, lowercase, digits, and special characters.
  """

  uppercase = 0
  lowercase = 0
  digits = 0
  special_chars = 0

  for char in string:
    if char.isupper():
      uppercase += 1
    elif char.islower():
      lowercase += 1
    elif char.isdigit():
      digits += 1
    else:
      special_chars += 1

  return {
    "uppercase": uppercase,
    "lowercase": lowercase,
    "digits": digits,
    "special_chars": special_chars
  }

# Example usage
string = "Hello123@#"
character_counts = count_characters(string)

print("Character counts:")
for char_type, count in character_counts.items():
  print(f"{char_type}: {count}")

#Number 49
def can_be_rearranged(str1, str2):
  """
  This function checks if the characters in one string (str1) can be rearranged to form another string (str2).

  Args:
      str1: The first string.
      str2: The second string.

  Returns:
      True if str1 can be rearranged to form str2, False otherwise.
  """

  # Check if strings have the same length, otherwise rearrangement is impossible
  if len(str1) != len(str2):
    return False

  # Use a dictionary to count character occurrences in both strings
  char_counts = {}
  for char in str1:
    char_counts[char] = char_counts.get(char, 0) + 1
  for char in str2:
    if char not in char_counts or char_counts[char] == 0:
      return False
    char_counts[char] -= 1

  return True

# Example usage
str1 = "listen"
str2 = "silent"
if can_be_rearranged(str1, str2):
  print(f"{str1} can be rearranged to form {str2}")
else:
  print(f"{str1} cannot be rearranged to form {str2}")
