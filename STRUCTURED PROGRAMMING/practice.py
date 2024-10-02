# print("****A program to add numbers****")

# num1 = int(input("Enter the first number: "))
# num2= int(input("Enter the second number: "))
# sum = (num1+ num2)
# print(sum)

# user_input = (input("Enter an expression: "))
# calc = eval(user_input)
# print(calc)

length = int(input("Enter the length of the cuboid: "))
width = int(input("Enter the width of the cuboid: "))
height = int(input("Enter the height of the cuboid: "))

def calculate_area(l,w,h):
    area = l*w*h
    return area

print("the area is",calculate_area(length,width,height))



   