#number 39
# Enter a number from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
    
    
#Number 50
# Define the number of rows for the pattern
rows = 10

# Generate the pattern
for i in range(rows):
    for j in range(i, -1, -1):
        print(j, end="")
    print()

