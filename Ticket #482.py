user_name = input("Name? ").strip()
mood = input("Payment method? (card/cash): ").lower()
if mood == "card":
    print("Processing...").lower()
else:
    message = "Cash accepted".upper()
    print(message)
