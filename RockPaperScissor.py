import random

x = int(input("\nLet's play rock-paper-scissor! Best out of? "))
p = 0
c = 0

if x % 2 == 0:
	y = (x/2) + 1
else:
	y = (x/2)


while p < y and c < y:
	print(f"\n*** Score - Computer: {c} Player: {p} ***\n")
	options = {1:"rock", 2:"paper", 3:"scissors"}
	com = options[random.randint(1,3)]
	p1 = input("Make a move!: ").lower()

	print(f"\nComputer plays: {com}")

	if p1:
		if p1 == com:
			print("Its a tie!!")
		elif p1 == "rock":
			if com == "scissor":
				print("Player wins!")
				p += 1
			elif com == "paper":
				print("Computer wins!")
				c += 1
		elif p1 == "scissor":
			if com == "rock":
				print("Computer wins!")
				c += 1
			elif com == "paper":
				print("Player wins!")
				p += 1
		elif p1 == "paper":
			if com == "scissor":
				print("Computer wins!")
				c += 1
			elif com == "rock":
				print("Player wins!")
				p += 1
		else:
			print("You made an invalid move.")
	else:
		print("You need to make a move.")
if p > c:
	print("\nPlayer won!")
	print(f"Final Score - Computer: {c} Player: {p}\n")
elif p < c:
	print("\nComputer won!")
	print(f"Final Score - Computer: {c} Player: {p}\n")