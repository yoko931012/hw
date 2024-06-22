print("Welcome to the simple calculator program!")

while True:
	first_number = float(input("Enter the first number:"))
	second_number = float(input("Enter the second number:"))
	select = str(input("Select an arithmetic operation(+, -, *, /):"))
	
	if select == "+":
		print("Result :" ,first_number + second_number)
	if select == "-":
		print("Result :" ,first_number - second_number)	
	if select == "*":
		print("Result :" ,first_number * second_number)	
	if select == "/" and second_number == 0:
		print("Error:Division by zero!")
		continue
	
	if select == "/" and second_number != 0:	
			print("Result :" ,first_number / second_number)
			
	another = input("Do you want to perform another calculation?(yes or no):")
	if another != "yes":
   	    print("Goodbye!")	
   	    break	
  		

	