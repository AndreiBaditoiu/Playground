print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15\n"))
people = int(input("How many people to split the bill?\n"))
tip_percentage = tip / 100
total_bill_with_tip = bill * (1 + tip_percentage)
split = total_bill_with_tip / people

print(f"Each person should pay: ${split:.2f}")


