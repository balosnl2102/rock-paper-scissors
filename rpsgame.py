#Name
#Rock, Paper, Scissors Game
#____________________________________________________________________________
#break into pieces
#Welcome page, with name entry
#Score screen with Computer, player (name), ties
#Options for game r, p, s, q
#Game will loop until q is entered
#Each loop will get a random choice from the computer
#A choice from the player, compare the two, and update the score
#When the game is over (q is entered) final score is displayed

#Welcome PAGE
#Prompt for the player name
#A welcome message

#_____________________________________________________________________________

#imports:
import random
#variables
playerScore = 0
computerScore = 0
ties = 0
#make a list
cChoices = ["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name: ")
print("Welcome " + name + ". Good Luck!")
# main loop
while True:
	#print score
	print("Score:")
	print("Computer: " + str(computerScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for paper, 's' for scissors, or 'q' for quit: ")
	computerChoice = random.choice(cChoices)	

	if choice == "q":
		print("Thanks for playing!")
		break

	if choice == "r":
		print(name + " Picked Rock")
		if computerChoice == "r":#tie
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock")
			computerScore += 1
		else: # s is only choice left
			print("Computer picked Scissors")
			print("Rock beats Scissors")
			playerScore += 1
	elif choice == "p":
		print(name + " Picked Paper")
		if computerChoice == "r":#tie
			print("Computer picked Rock")
			print("Paper beats Rock")
			playerScore += 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		else: # s is only choice left
			print("Computer picked Scissors")
			print("Scissors beats Paper")
			computerScore += 1
	elif choice == "s":
		print(name + " Picked Scissors")
		if computerChoice == "r":#tie
			print("Computer picked Rock")
			print("Rock beats Scissors")
			computerScore += 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Scissors beats Paper")
			playerScore += 1
		else: # s is only choice left
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
	else: #print something else
		print("Please choose from either 'r', 'p', 's', or 'q'")