#Number 3
# Define the number of rows for the pattern
rows = 5

# Generate the upper part of the pattern
for i in range(1, rows + 1):
    for j in range(i):
        print("#", end="")
    print()

# Generate the lower part of the pattern
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("#", end="")
    print()


#Number 4
# Accept a word from the user
word = input("Enter a word: ")

# Reverse the word using slicing
reversed_word = word[::-1]

# Print the reversed word
print("Reversed word:", reversed_word)
