from random import randint

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
comp = ''
if guessInLower == 'x':
	yours = 'x'
	comp = 'o'
else:
	yours = 'o'
	comp = 'x'
print '************************************************************'
print
print 'Yours is \'',yours, '\' and Computer\'s is', " \'", comp,'\'' 
print
print '************************************************************'
print
# Display board
show()
print