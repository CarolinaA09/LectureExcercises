#!/usr/bin/python3

import os
import sys



dictonary={}
dictonary["Name"]=input("what is yout name ")
dictonary["color"]=input("what is your favorite color ")
dictonary["age"]=input("how old are you " )
dictonary["Python"]=input("do you like python ")
dictonary["World"]=input("Worl is flat true or false ")

#dictionary={ name:input("what is yout name "), age:input("how old are you " ), color:input("what is your favorite color "), Python:input("do you like python "), world:input("Worl is flat true or false ")

def questions_to_user(dictonary):
	if dictonary["Name"] == "yes":
		print("you are stupid")
	else:
		print("I like you")
	if int(dictonary["age"]) > int(25):
		print("you are old")
	else:
		print("you are fine")
	print("I am " + dictonary["Name"] + " and my favorite color is " + dictonary["color"])
	if dictonary["World"] == True:
		print("Your are wrong")
	else:
		print("You are right")

	return 0

questions_to_user(dictonary)




#dictionary={}i
#dictonary["Name"]=input("what is yout name ")
#dictonary["color"]=input("what is your favorite color ")
#dictonary["age"]=input("how old are you " )
#dictonary["Python"]=input("do you like python ")
#dictonary["World"]=input("Worl is flat true or false ")
