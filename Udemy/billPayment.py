print("Welcome to tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would like to give? 10, 12, or 15? "))
split_bill = float(input("How many people to split the bill?"))

total_bill = tip_percentage / 100 * bill + bill

split_bill_person = total_bill / split_bill

print(f"Total bill {total_bill:.2f}")
print(f"Each person should pay: {split_bill_person:.2f}")