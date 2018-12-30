import random

# Most of this stuff is commented out.  
# Part of the reason is through an eXtreMe programming approach and I wanted to preserve my thought process which currently is defeloped for functions.
# Part of it is also that I apperently don't kow how the 'return' script works between functions.
# So preserving this part of the code may also aid in showing progress as a programmer once I'm more fluent in the logic.
# I'd like to return to this code one day to make it work through functions.
# Until then, copy-pasting everything into the Main() function seems to work just fine.

#def DefineDieType():
#	die_sides = int(input("How many sides to the die? >"))
#	return die_sides
#
#def RollDie():
#	roll = random.randint(1, die_sides)
#	return roll
#
#def RollMultipleDice():
#	number_of_dice = int(input("How many dice are being rolled? >"))
#	dice_rolled = 0
#
#	global total_from_dice
#
#	while dice_rolled < number_of_dice:
#		RollDie()
#		total_from_dice += roll
#		dice_rolled +=1
#
#def AddModifier():
#	modifier = int(input("What is the modifier? >"))
#	global total_from_dice
#	total_from_dice += modifier

def Main():
	while True:
		total_from_dice = 0

		die_sides = int(input("How many sides to the die? >"))
		number_of_dice = int(input("How many dice are being rolled? >"))
		dice_rolled = 0

		while dice_rolled < number_of_dice:
			total_from_dice += random.randint(1, die_sides)
			dice_rolled +=1

		modifier = int(input("What is the modifier? >"))
		total_from_dice += modifier

		print("\n Result: ", total_from_dice)

Main()