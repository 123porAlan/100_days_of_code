print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? " ))
people = int(input("How many people to split the bill? "))
total_tip_amount = tip / 100 * bill
bill_with_tip = bill + total_tip_amount
bill_per_person = round(bill_with_tip / people,2) # This is float
# Convert to string wiht the same format, which is two decimal places
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}")
