import random
print("Let's roll the dice!")
i = 'y'
while i == 'y':
	x = random.randint(1,6)
	if x==1:
		print(" ---------")
		print("|         |")
		print("|    O    |")
		print("|         |")
		print(" ---------")
	if x==2:
		print(" ---------")
		print("|         |")
		print("|   O O   |")
		print("|         |")
		print(" ---------")

	if x==3:
		print(" ---------")
		print("|    O    |")
		print("|    O    |")
		print("|    O    |")
		print(" ---------")

	if x==4:
		print(" ---------")
		print("|  O   O  |")
		print("|         |")
		print("|  O   O  |")
		print(" ---------")

	if x==5:
		print(" ---------")
		print("|  O   O  |")
		print("|    O    |")
		print("|  O   O  |")
		print(" ---------")

	if x==6:
		print(" ---------")
		print("| O  O  O |")
		print("|         |")
		print("| O  O  O |")
		print(" ---------")

	i = input("Press 'y' for rolling again: ")

