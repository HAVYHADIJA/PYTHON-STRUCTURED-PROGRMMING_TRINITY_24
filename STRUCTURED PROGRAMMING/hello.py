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