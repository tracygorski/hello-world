#Pull middle two (for even) or middle three (for odd) characters of user input
print("Ready to see the middle characters of your input?")
answer = None 
while answer not in ("yes", "no"): 
	answer = input("Enter yes or no: ")
	if answer.lower().strip() == "yes": 
		midinput = input("Enter an input:")
		def middle_char(txt):
			return txt[(len(txt)-2)//2:(len(txt)+3)//2]
		print("Result:" + middle_char(midinput))
		print("Have a great day!")
		quit()
	elif answer.lower().strip() == "no": 
		print("Maybe next time. Have a great day!")
		quit()
	else: 
		print("Please enter yes or no.")
		
