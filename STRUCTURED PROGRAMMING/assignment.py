#loop countdown
num = 10
while num >0:
    print(num)
    num = num-1
    
#number 2
n = 1  
sum_numbers = 0
count = 0

while count < 20:
    sum_numbers += n
    n += 1
    count += 1

print("Sum of the first 20 natural numbers:", sum_numbers)

#number 3
#even numbers
e_num = 0
while  e_num<= 50:
    print(e_num)
    e_num = e_num + 2
    

#number 4
password = "1234"
attempts = 3
while attempts >0:
    user_input=input("Please enter password ")
    if user_input==password:
        print("Access granted")
        break
    else:
        attempts=attempts-1
        print("Incorrect password")
        if attempts==0:
            print("Login failed")

#number 6

sum = 0
numb = None
while True:
    try:
        num = int(input("Enter a number (enter 0 to stop): "))
        if num == 0:
            break  
        sum += num 
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"The sum of all numbers entered is: {sum}")

#number 7
# input a number from the user
numb = int(input("Enter a number to print its multiplication table: "))

m = 1

# While loop to print multiplication table up to 10
while m <= 10:
    result = numb * m
    print(f"{numb} * {m} = {result}")
    m = m +1


#number 5
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  
    if num % 2 == 0:
        return False  
    
    # Check for odd factors from 3 up to the square root of num
    factor = 3
    while factor * factor <= num:
        if num % factor == 0:
            return False
        factor += 2  
    return True

# Using a while loop to print all prime numbers less than 20
num = 2  # Start with the smallest prime number
while num < 20:
    if is_prime(num):
        print(num)
    num += 1


    
    