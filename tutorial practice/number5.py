#A Program that checks if a store offers free delivery
total_order = float(input("Enter the total amount of the order: "))
if total_order < 100000:
    print("Free delivery")
else:
    delivery_fee = 0.05* total_order
    print(f"The delivery fee is{delivery_fee}UGX")
paid_amount = float(input("Enter the amount paid in UGX: "))
if paid_amount >= delivery_fee:
    print("Coming right up")
else:
    print("Please pay some more")