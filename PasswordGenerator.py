#Created By Sanaan Wani Contact:sanaan1000@gmail.com

import random
print("Let me enlighten you about password cracking.")
print("Lets take an example of the password 'letmein'")
print("You will also see some reasons why letmein isnt a good password to use:")
print("It’s a very common password-one of the 15 most used passwords.")
print(" A computer would guess these first.")
print("It contains words from the dictionary.")
print("A computer would also try these passwords first.")

print("It’s very short. It would take a computer more time to guess a longer password.")

print("It only contains letters. Passwords are more secure if they also contain numbers and punctuation.")
chars = "abcdefghijklmnopqrstuvwxyz1234567890"
print("")
length = input("So now what Password Length do you want? ")
length = int(length)
number = input("How many passwords do you want?")
number = int(number)
for p in range(number):
	password = ""
	for c in range(length):
		password += random.choice(chars)
	print("NewPassword:",password)