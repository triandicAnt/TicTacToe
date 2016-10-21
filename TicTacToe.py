from random import randint
import random

# Create Board
board = range(0,9)

# show board
def show():
	print board[0],'|',board[1],'|',board[2]
	print '----------'
	print board[3],'|',board[4],'|',board[5]
	print '----------'
	print board[6],'|',board[7],'|',board[8]

print '************************************************************'
print 
# Select the mark
while True:
	userInput = raw_input('Please select your mark: \'x\' or \'o\' :')
	if userInput!='x' and userInput!='o':
		print 'Invalid choice!'
	else:
		break

guessInLower = userInput.lower()
print
print '************************************************************'
print

yours = ''
comps = ''

if guessInLower == 'x':
	yours = 'x'
	comps = 'o'
else:
	yours = 'o'
	comps = 'x'

print '************************************************************'
print
print 'Yours is \'',yours, '\' and Computer\'s is', " \'", comps,'\'' 
print
print '************************************************************'
print

# Display board

show()
print

#check for winner

def checkline(char, spot1, spot2, spot3):

	if board[spot1] == char and board[spot2] == char and board[spot3] == char:
		return True

def checkWinner(char):

	if checkline(char, 0,1,2):
		return True
	if checkline(char, 3,4,5):
		return True
	if checkline(char, 6,7,8):
		return True
	if checkline(char, 0,3,6):
		return True
	if checkline(char, 1,4,7):
		return True
	if checkline(char, 2,5,8):
		return True
	if checkline(char, 0,4,8):
		return True
	if checkline(char, 2,4,6):
		return True

# Start Game

while True:
	input = raw_input('Select a spot: ')
	input = int(input)

	if board[input] != yours and board[input] != comps:
		board[input] = yours


		# check for winner

		if checkWinner(yours) == True:
			print
			print '~~~~~ You Win!    ~~~~~'
			print '~~~~~ Game Over!  ~~~~~'
			print
			show()
			print

			break

		# computer's turn
		# generate a random number between 0 and 8
		# fill the spot for that random number

		compWins = False

		while True:
			random.seed()
			opponent = random.randint(0,8)

			# fill the spot
			if board[opponent] != yours and board[opponent] != comps:
				board[opponent] = comps

				# check for winner

				if checkWinner(comps) == True:
					print
					print '~~~~~ Computer Wins! You are a loser!! ;) ~~~~~'
					print '~~~~~ Game Over! ~~~~~'
					print
					compWins = True
					break

				break
		
		if compWins == True:
			show()
			print
			break

	else:
		print 'This spot is occupied! Select another: '

	print

	# display board
	show()
	print


