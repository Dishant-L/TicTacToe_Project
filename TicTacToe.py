board = [' ' for x in range(10)]
def insertLetter(letter,pos):
	board[pos] = letter

def spaceIsFree(pos):
	return board[pos] == ' '

def printBoard(board):
	print('   |   |  ')
	print('  '+board[1]+'| '+board[2]+' | '+board[3])
	print('   |   |  ')
	print('-----------')
	print('   |   |  ')
	print('  '+board[4]+'| '+board[5]+' | '+board[6])
	print('   |   |  ')
	print('-----------')
	print('   |   |  ')
	print('  '+board[7]+'| '+board[8]+' | '+board[9])
	print('   |   |  ')

def isWinner(bo,le):
	return (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3]==le) or (bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le)

def playerMove():
	run = True
	while run:
		move = input('Select Your Position')
		try:
			new_move = int(move)
			print(new_move)
			if (new_move>0 and new_move<10):
				if spaceIsFree(new_move):
					run = False
					insertLetter('X',new_move)
				else:
					print('This space is already occupied by Computer')
			else:
				print('Please Enter a number between (1-9)')
		except:
			print('Please Enter a number')

def compMove():
	possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
	move = 0
	for let in ['O','X']:
		for i in possibleMoves:
			boardCopy = board[:]
			boardCopy[i] == let
			if isWinner(boardCopy,let):
				move = i
				return move

	cornersOpen = []
	for i in possibleMoves:
		if i in [1,3,7,9]:
			cornersOpen.append(i)
	if len(cornersOpen) > 0:
		a = selectRandom(cornersOpen)
		move = cornersOpen[a]
		return move

	if 5 in possibleMoves:
		move = 5
		return move

	edgesOpen = []
	for i in possibleMoves:
		if i in [2,4,6,8]:
			edgesOpen.append(i)
	if len(edgesOpen) > 0:
		c = selectRandom(edgesOpen)
		move = edgesOpen[c]
	return move

def selectRandom(li):
	import random 
	ln = len(li)
	r = random.randrange(0,ln)
	return r

def isBoardFull(board):
	if board.count(' ')>1:
		return False
	else:
		return True

def main():
	print('Welcome To Tic Tac Toe!!!')
	printBoard(board)
	while not(isBoardFull(board)):
		if not(isWinner(board, 'O')):
			playerMove()
			printBoard(board)
		else:
			print('Computer Wins')
			break

		if not(isWinner(board, 'X')):
			move = compMove()
			if move == 0:
				print('We have a TIE Game')
			else:
				insertLetter('O',move)
				print('Computer played its move')
				printBoard(board)
		else:
			print('You Win')
			break
	if isBoardFull(board):
		print('We have a TIE Game')


main()

		


		
		
		


