#A program to check if person is eligible to vote in Uganda
age = int(input("Enter the age of the voter: "))
citizenship = input("Are you are citizen of Uganda? (yes/no): ")
reg_status = input("Are you a registerd voter? (yes/no): ")
if age >= 18 and citizenship == "yes":
    if reg_status == "yes":
        print("The person is eligible to vote")
    