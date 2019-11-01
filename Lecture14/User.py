#!/usr/bin/python3

import os

os.system("clear")

print("\n\nImported os\n\n")

#Function to process and catch the details that the user provides
#Arguments will come in as list from the dictionary of details provided

def personal (name, age, col, py, world):
	import string
	print("You have provided the following details: \n\tName: ",name,"\n\tAge: ",age,"\n\tFave colour: ",col,"\n\tPython preference: ",py,"\n\tFlat world: ",world)
	for character in name:
		if character not in string.ascii_letters:
			return print("\nYou are not a number, honestly, please start again!")
	if age > 99 or age < 3:
		return print(("\nYou are not a number, honestly, please start again!")
	if col.upper() != "BLACK":
		print ("\nI really like black, but",col,"is OK too!")
	else:
		print("\nI really like black too, excellent choice!")
	if py.upper()[0] != "Y":
		print("\nI am sorry that you dont like Python")
	else:
		print("\nGlad you agree that Python is cool...")
	if world != "False":
		return print("\nEither you really DO think the world is flat (it isnt),\nor you havent typed False in the correct Python format...\n\n")
	return "OK", print("\nAll OK, thanks a lot.")

#Process:interact with the user, storing the output in an ordered dictionary

#Check the questions are in the right order for the function (or modify fuction)

details["Name"]=input("Hi, what is your name?")
details["Age"]=int(input("How old are you?")
details["Color"]=input("What's your favourite colour?")
details["Python"]=input("Do you like Python?")
details["World"]=input("The world is flat: True or False?")

personal(*list(details.values()))

print("\n\nThis was the dictionary you set up...\n\n",details,"\n\nBye!\n\n")

exit()

