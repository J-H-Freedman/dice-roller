# Simple dice roller using a series of functions.

import random

# Get values
def GetDieTypeFromUser():
	return int(input("How many sides to the die? >"))
	
def GetNumberOfDiceFromUser():
	return int(input("How many dice are being rolled? >"))

def GetModifierFromUser():
	return int(input("What is the modifier? >"))

# Roll dice
def RollMultipleDice(number_of_dice, die_sides):
	dice_rolled = 0
	total_from_dice = 0

	while dice_rolled < number_of_dice:
		total_from_dice += random.randint(1, die_sides)
		dice_rolled += 1

	return total_from_dice	

def Main():
	# Lasts until crash.  Type a non-int to crash deliberately.
	while True:
		# Get values
		die_sides = GetDieTypeFromUser()
		number_of_dice = GetNumberOfDiceFromUser()
		modifier = GetModifierFromUser()
		
		# Calculate and print
		total_from_dice = RollMultipleDice(number_of_dice, die_sides)
		print("... \n Rolling ", number_of_dice, "d", die_sides, ": \n", total_from_dice, "\n \n", total_from_dice, "+ Modifier(", modifier, ") :")
		total_from_dice += modifier
		print("--->", total_from_dice, "<--- \n ", "...")

Main()
