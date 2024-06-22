shopping_amount = float(input("Enter the shopping amount:"))
membership_level = str(input("Enter the membership level (Regular or Gold):"))
if membership_level == "Regular":
	if shopping_amount > 3000:
		discount = 0.2
	elif shopping_amount > 2000:
		discount = 0.15
	elif shopping_amount > 1000:
		discount = 0.1
	else:
		discount = 0
elif membership_level == "Gold":
	if shopping_amount > 3000:
		discount = 0.25
	elif shopping_amount > 2000:
		discount = 0.2
	elif shopping_amount > 1000:
		discount = 0.15
	else:
		discount = 0
else:
	print("Invalid membership level. Please enter 'Regular' or 'Gold'.")		
final_amout = shopping_amount - (shopping_amount*discount)
print(membership_level, "$",final_amout)
