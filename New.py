#Login System with Attempts 
correct_username = "admin"
correct_password = "1234"
attempts = 0
on = True
while on :
	username = input("enter your user name : ")
	password = input("enter your password : ")
	if username == "admin" and password == "1234" :
		print("login successful")
		on = False
	if username != "admin" and password != "1234" :
		
		attempts += 1
		print("___________________________")
		if attempts == 3 :
			on = False
if not on :
	print("////////Account Blocked///////")
