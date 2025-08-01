import random
computer_wins = 0
user_wins = 0
options = ["rock","paper","scissors"]
while True:
	user_pick = input('Chose one from ("Rock","Paper","Scissors") or **Q** to (Quit): ').lower()
	
	if user_pick == "q":
		break
	
	if user_pick not in options:
		print("Invalid input, please try again.")
		continue
	
	random_number= random.randint(0,2)
	computer_pick = options[random_number]

	print ("Computer Picked ", computer_pick)

	if user_pick == computer_pick:
		print("Tie")
	elif (user_pick == "rock" and computer_pick == "scissors") or (user_pick == "paper" and computer_pick == "rock") or (user_pick == "scissors" and computer_pick == "paper"):
		print("You won")
		user_wins += 1
	else:
		print("Computer won")
		computer_wins += 1
	
print("Game Score:")
print("Computer won",computer_wins,"Times.")
print("You won",user_wins,"Times.")

if user_wins == computer_wins:
	print("Tie")
elif user_wins > computer_wins:
	print("Congratulations, you won the entire game!!!")
elif user_wins < computer_wins:
	print("Better luck next time!!")

print("Good Bye!!")