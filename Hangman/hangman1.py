import random
 
wordlist = 'animal, apple, awesome, amazing, ball, best, beat, been, came, cent,'.upper().split()
random.shuffle(wordlist)

hangman_board = ['''
PLACEHOLDER #0 - ZERO MISSES''','''
PLACEHOLDER #1 - FIRST MISS''','''
PLACEHOLDER #2 - SECOND MISS''','''
PLACEHOLDER #3 - THIRD MISS''','''
PLACEHOLDER #4 - FOURTH MISS''','''
PLACEHOLDER #5 - FIFTH MISS''']

secret_word = wordlist.pop()
correct = []
incorrect = []

print("DEBUG: %s" % secret_word)
def Draw_bord():
	#draw the gallows eventually and displays the words
	print(hangman_board[len(incorrect)])
	for i in secret_word:
		if i in correct:
			print (i, end = ' ')
		else:
			print('_', end =' ') 
	print("\n\n")
	print("***Missed Letters***")
	for i in incorrect:
		print(i, end =' ')
	print("\n***********************")


def user_guess():
	#allows the user to give out a guess. append that letter to correct or incorrect
	while True:
		guess = input  ("guess a letter\n:").upper()
		if guess in correct or guess in incorrect:
			print("You have already guessed that letter. Guess again")
		elif guess.isnumeric():
			print("Please enter only letters not numbers. Guess again ")
		elif len(guess) > 1:
			print("Please enter one letter at a time. Guess again")
		elif len(guess) == 0:
			print("Please enter your selection")
		else:
			break

	if guess in secret_word:
		correct.append(guess)
	else:
		incorrect.append(guess)

def check_win():
	#checks/confirms to see if the user has won or lost the game.
	if len(incorrect) > 5:
		return 'loss'

while True:
	Draw_bord()
	user_guess()