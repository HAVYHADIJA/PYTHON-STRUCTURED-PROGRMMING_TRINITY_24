#number 8
#input a number from the user
numb = int(input("Enter a number to print its multiplication table: "))

m = 1
 #While loop to print multiplication table of 5
while m <= 10:
    result = numb * m
    print(f"{numb} * {m} = {result}")
    m = m +1
    
    
#Number 2
import random

# Generate a random number between 1 and 20 (inclusive)
number = random.randint(1, 20)

while True:
  # Prompt the user for a guess
  guess_str = input("Guess a number between 1 and 20: ")

  # Convert the guess from a string to an integer
  try:
    guess = int(guess_str)
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue

  # Check if the guess is correct
  if guess == number:
    print("Well guessed!")
    break  # Exit the loop

  # Provide feedback based on the guess
  elif guess < number:
    print("Too low, try again.")
  else:
    print("Too high, try again.")


