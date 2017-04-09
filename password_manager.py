from Crypto.Cipher import AES
import strgen
from ast import literal_eval

def store_credentials_to_file(user_name,password):
	website = raw_input("\nEnter the name of the  websites you want to store credentials for:\n")
	strong_password = strgen.StringGenerator("[\d\w]{24}").render()
	
	text = str(strong_password) + "aaaaaaaa"
	
	key = password
	encryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
	cipher_text = encryption_suite.encrypt(text)
	saved_cipher = repr(cipher_text)
	f = open("user_%s" %user_name, 'a+')
	f.write(website + "and" + saved_cipher)
	f.write("\n")
	f.close()

def new_user():
	
	user_name = raw_input(" Enter a new user name\n")
	password = raw_input(" Enter the password \n Requirements - Should be 16 characacters\n")
	confirm_password = raw_input(" Confirm your password :\n")
	if len(password) != 16 or password != confirm_password:
		print " Invalid password"
		return 100
	else:
		f = open("user_%s" %user_name, 'w+')
		f.write(user_name + "and" + password)
		f.write("\n")
		f.close()
	
	user_choice = raw_input(" \nDo you want to store credentials for websites now, press y for yes and n for no\n")

	if user_choice =="y":
		
		store_credentials_to_file(user_name, password)
	elif user_choice =="n":
		print " Alright, see you next time"
	else:
		print " Wrong choice"

def existing_user():
	count = 1
	username = raw_input(" \nEnter the username :")
        password = raw_input("\n Enter the password:")
	val_return = validate_user(username,password)
	user_choice = int(raw_input(" \n What operation do you want to perform :\n Enter 1 for fetching credentials for a website and Enter 2 for entering registering passwords for a new website \n "))
	if user_choice == 1:
		while(count < 5):
		
			if val_return ==True:
				website = raw_input("\n For which website do you want to fetch the credentials:")
				avail_password(website,password,username)
				count+=1
			else :
				print( "\n Credentials don't match, enter username and password again")
			
	if user_choice == 2:
		store_credentials_to_file(username, password)
	
	else:	
		print ("\nUser doesn't want to perform any further operation \n")
	
	return True
def validate_user(username, password):
	f = open("user_%s" %username, 'r+')
	line_1 = f.readline()
	u,p = line_1.split("and")
	p = p[0:16]
	if u == username and p == password:
		print "Credentials verified for %s" %username
		return True
	else:
		return False
	

def avail_password(website,password, username):
	key = password
	fa = open("user_%s" %username, 'r+')
	for line in fa:
		a,b = line.split("and")
		if a ==website:
			cipher_text = literal_eval(b)
			#cipher_text = cipher_text[0:(len(cipher_text)-1)]
			
			decryption_suite = AES.new(password, AES.MODE_CBC, 'This is an IV456')
			print len(cipher_text)
			plain_text = decryption_suite.decrypt(cipher_text)
	
			plain_text = plain_text[0:24]
			print " \nThe password for website :", website, " is ", plain_text
	fa.close()
	
        	
	
def main():
	print " Welcome to the Password Manager system \n You have the below options \n \n1. New User \n 2. Existing user\n"
	user_input= raw_input("\nSelect your choice\n")
	if user_input == "1":
		val_return = new_user()
		while(val_return ==10):
			print " User has to enter the credentials again "
			val_return = new_user()
		
	elif user_input =="2":

		val_return = existing_user()

if __name__ == "__main__":
  main()




