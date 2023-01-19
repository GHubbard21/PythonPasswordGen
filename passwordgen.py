import random
import secrets
import string
import time



lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = string.digits
symbols = string.punctuation



alphabet = lower + upper + nums + symbols

print("Hello and welcome to this password generator")
time.sleep(2.0)
print("Enter a number for how long you want your password to be")
length = int(input())


# Check that the input is a valid integer
if length <= 0:
	print("Please input a valid integer")
	length = int(input())

# Confirmation on Length of Password
print("Are you Sure? Y/N")

confirm = input()


if confirm == "Y" or confirm =="y":
	
		temp = random.sample(alphabet,length)
		pw = "".join(temp)

		print(pw)
	
else:
		print("Okay, goodbye.")



# IM LOSING MY MIND


	

