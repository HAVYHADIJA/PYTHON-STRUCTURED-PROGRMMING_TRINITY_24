#A Program to determine the type of weather
temp =  float(input("Enter the temperature in Entebbe: "))
if temp > 30:
    print("Hot")
elif temp >=20 and temp <=30:
    print("Warm")
elif temp < 20:
    print("cool")
    