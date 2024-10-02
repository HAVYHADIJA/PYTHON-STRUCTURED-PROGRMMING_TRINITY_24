#Number 44
# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Read an integer representing a year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
    
#number 6
# Loop through the numbers from 0 to 10
for num in range(11):
    # If the number is 4 or 8, skip the rest of the loop and continue with the next iteration
    if num == 4 or num == 8:
        continue
    # Print the number
    print(num, end=" ")

