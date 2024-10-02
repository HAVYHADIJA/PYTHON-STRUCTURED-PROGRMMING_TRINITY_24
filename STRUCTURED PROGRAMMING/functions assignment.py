
#NAKALYOWA HADIJAH M24B13/029  B27519

# 1. Write a Python function to find the maximum of three numbers.
def max_of_three(a, b, c):
    return max(a, b, c)

# 2. Write a Python function to sum all the numbers in a list.
def sum_list(numbers):
    return sum(numbers)

# 3. Write a Python function to multiply all the numbers in a list.
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# 4. Write a Python program to reverse a string.
def reverse_string(s):
    return s[::-1]

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 6. Write a Python function to check whether a number falls within a given range.
def in_range(n, start, end):
    return start <= n <= end

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count



    
   