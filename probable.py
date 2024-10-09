#Module import
import backend

#Print suggestions
def suggestions(sugg):
	print('\n\u001b[34m+--------------+\n|\u001b[0m Rank \u001b[34m|\u001b[0m Word  \u001b[34m|\n+--------------+\u001b[0m')

	for i,s in enumerate(sugg):
		if len(str(i+1)) == 1:
			print(f'\u001b[34m|\u001b[0m  {i+1}   \u001b[34m|\u001b[0m {s[0]} \u001b[34m|\u001b[0m')
		else:
			print(f'\u001b[34m|\u001b[0m  {i+1}  \u001b[34m|\u001b[0m {s[0]} \u001b[34m|\u001b[0m')

	print('\u001b[34m+--------------+\n\u001b[0m')

#Input and response procedure
def guess(count):
	#Handling user input guess
	g = input(f'Guess {count}: ')
	while len(g) != 5:
		if g.upper() == 'X':
			exit()
		else:
			print('\u001b[33mThe guess must be 5 characters long.\u001b[0m')
			g = input(f'Guess {count}: ')

	#Handling user input response
	r = input(f'Response {count}: ')
	allowed = True
	for l in r:
		if l.isalpha() == False and l != '?':
			allowed = False
	if len(r) != 5:
		allowed = False

	while allowed == False:
		print('\u001b[33mThe response must be 5 characters long and follow the format laid out above.\u001b[0m')
		r = input(f'Response {count}: ')
		allowed = True
		for l in r:
			if l.isalpha() == False and l != '?':
				allowed = False
		if len(r) != 5:
			allowed = False

	sugg = solver.return10(g, r)

	suggestions(sugg)

#Program title
print('\n\u001b[34m█▀█ █▀█ █▀█ █▄▄ ▄▀█ █▄▄ █░░ █▀▀\n█▀▀ █▀▄ █▄█ █▄█ █▀█ █▄█ █▄▄ ██▄\u001b[0m\n')

#Instructions
print('=--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--=\n\nWelcome to Probable! This terminal application is designed to provide\nthe most statistically useful guesses at each stage throughout a Wordle\ngame.')
print('\nAfter each guess the user will be prompted to enter the guess and the\nresult from Wordle. The result should be provided in the following format:')
print('\nGrey squares should be displayed at ?, yellow as lower case letters, and\ngreen as upper case letters.')
print('\nThe input of ???tH would therefore correspond to three incorrect letters,\na successful but incorrectly positioned t, and a successful and\ncorrectly positioned h.')
print('\nOnce the user guess and Wordle response have been entered the top 10\nstatistically preferable guesses shall be returned. If the game has\nfinished simply enter X as the following guess to exit.')
print('\n=--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--=\n')

#Initialising solver
solver = backend.solver()

#Running game
for i in range(6):
	guess(i+1)