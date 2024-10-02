#number1
temperatures = [23, 25, 27, 22, 26, 24, 28]

# Calculate the average temperature using a while loop
total_sum = 0
count = 0
while count < len(temperatures):
    total_sum += temperatures[count]
    count += 1

average_temperature = total_sum / len(temperatures)

print(f"The average temperature in Kampala for the week is: {average_temperature}")

#number 2
