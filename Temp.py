#Number Guessing Game 
secret = "7"
attempt = 1
run = True
while run :
	guess = input("enter you guess number :")
	print(f"your attempts {attempt}")
	print("________________________________")
	if guess > secret :
		attempt += 1
		print("to high")
	elif guess < secret :
		attempt += 1
		print("too low")
	elif guess == secret :
		run = False
		print("/////////you won\\\\\\\\\")
 
	
