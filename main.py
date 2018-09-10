"""A class to represent the players."""
class Player:
	def __init__(self, name, colour):
		self.name = name
		
		# Assigns the integer representation depending on the colours.
		if colour == "yellow":
			self.intRep = 1
		elif colour == "red":
			self.intRep = 0
		else:
			print("Incorrect colour used, check Player object.")
	
	
"""A class to represent the board."""
class Board:
	def __init__(self, row=6, column=7):
		self.row = row
		self.col = column
		
		# None for null, 0 for yellow, 1 for red.
		self.discs = [[None for c in range(column)] for r in range(row)]
	

# Function prints the board based on the discs.
# It takes in the two players object and the board object.
def printBoard(p1, p2, board):
	print("", end="\n\n\n\n\n\n\n\n\n\n\n\n")
	
	# Print board based on discs in array.
	for r in range(board.row):
		print("  ", end="")
		for c in range(board.col):
			print("| ", end="")
			
			# If red,
			if board.discs[r][c] == p1.intRep:
				print("x", end="")
			# If yellow,
			elif board.discs[r][c] == p2.intRep:
				print("o", end="")
			# If null.
			else:
				print(" ", end="")
			
			print(" ", end="")
		print("|")
		
	# Print legs.
	print("  ", end="")
	for c in range(board.col):
		print("====", end="")
	print("=")
	
	# Print labels.
	print("  ", end="")
	for c in range(board.col):
		print("  " + str(c+1) + " ", end="")
	print("")
	
	
# Function places the respective player's discs on the board via the player's
# integer representation.
# It takes in the current player's object, the board and the column of the
# player's choice.
def placeDisc(player, board, columnOfChoice):
	# Search for the row/coordinates in the list where it is still None,
	# if None, we replace it with the player's integer representation.
	for r in range(board.row-1, -1, -1):
		if board.discs[r][columnOfChoice] is None:
			board.discs[r][columnOfChoice] = player.intRep
			break
		else:
			continue
	

# The following functions search each direction based on a coordinate and
# check if they satisfy the winning condition i.e. 4 similar discs in a row.
# It takes in the current player's object, the board and the coordinate that
# it starts searching from.

# Up
def searchNorth(player, board, startRow, startCol):
	# From current row to first/top row.
	for r in range(startRow, -1, -1):
		if board.discs[r][startCol] == player.intRep and startRow - r >= 3:
			return True
		elif not board.discs[r][startCol] == player.intRep:
			return False
	else:
		return False
	
# Up & Right		
def searchNorthEast(player, board, startRow, startCol):
	# From current row to first/top row.
	# From current column to rightmost column.
	for r, c in zip(range(startRow, -1, -1), range(startCol, board.col)):
		if board.discs[r][c] == player.intRep and startRow - r >= 3 and c - startCol >= 3:
			return True
		elif not board.discs[r][c] == player.intRep:
			return False
	else:
		return False
				
# Right
def searchEast(player, board, startRow, startCol):
	# From current column to rightmost column.
	for c in range(startCol, board.col):
		if board.discs[startRow][c] == player.intRep and c - startCol >= 3:
			return True
		elif not board.discs[startRow][c] == player.intRep:
			return False
	else:
		return False
			
# Down & Right
def searchSouthEast(player, board, startRow, startCol):
	# From current row to last/bottom row.
	# From current column to rightmost column.
	for r, c in zip(range(startRow, board.row), range(startCol, board.col)):
		if board.discs[r][c] == player.intRep and r - startRow >= 3 and c - startCol >= 3:
			return True
		elif not board.discs[r][c] == player.intRep:
			return False
	else:
		return False
				
# Down
def searchSouth(player, board, startRow, startCol):
	# From current row to last/bottom row.
	for r in range(startRow, board.row):
		if board.discs[r][startCol] == player.intRep and r - startRow >= 3:
			return True
		elif not board.discs[r][startCol] == player.intRep:
			return False
	else:
		return False
			
# Down & Left
# 3,4	6,1
def searchSouthWest(player, board, startRow, startCol):
	# From current row to last/bottom row.
	# From current column to leftmost column.
	for r, c in zip(range(startRow, board.row), range(startCol, -1, -1)):
		if board.discs[r][c] == player.intRep and r - startRow >= 3 and startCol - c >= 3:
			return True
		elif not board.discs[r][c] == player.intRep:
			return False
	else:
		return False
				
# Left
def searchWest(player, board, startRow, startCol):
	# From current column to leftmost column.
	for c in range(startCol, -1, -1):
		if board.discs[startRow][c] == player.intRep and startCol - c >= 3:
			return True
		elif not board.discs[startRow][c] == player.intRep:
			return False
	else:
		return False
			
# Up & Left
def searchNorthWest(player, board, startRow, startCol):
	# From current row to first/top row.
	# From current column to leftmost column.
	for r, c in zip(range(startRow, -1, -1), range(startCol, -1, -1)):
		if board.discs[r][c] == player.intRep and startRow - r >= 3 and startCol - c >= 3:
			return True
		elif not board.discs[r][c] == player.intRep:
			return False
	else:
		return False
			

# Function searches all the directions based on a particular coordinate and
# check for the winning condition.
# It takes in the current player object, the board object and the particular
# coordinate.
def searchDirections(player, board, row, col):
	directions = [searchNorth(player, board, row, col), searchNorthEast(player, board, row, col), searchEast(player, board, row, col), searchSouthEast(player, board, row, col), searchSouth(player, board, row, col), searchSouthWest(player, board, row, col), searchWest(player, board, row, col), searchNorthWest(player, board, row, col)]
	return any(directions)


# Function loops through the board and checks if there is a winning condition.
# It takes in the current player object and the board object.
def checkIfWin(player, board):
	for r in range(board.row):
		for c in range(board.col):
			if board.discs[r][c] == player.intRep:
				boolResult = searchDirections(player, board, r, c)
				if boolResult:
					return boolResult
					
					
# Functions checks if the chosen column is overflow, in which case, the player
# cannot place a disc at that column.
# It takes in the board object and the player's column choice.
def columnOverflow(board, columnOfChoice):
	# If the top most row of the chosen column is not filled yet.
	# If filled, means overflow.
	if board.discs[0][columnOfChoice] is None:
		return False
	else:
		return True
	
	
# Function handles the turn of the game, it returns the player's object that won.
# It takes in the two player objects and the board object.
def manageTurns(p1, p2, board):
	numTurns = 1
	while True:
		printBoard(p1, p2, board)
		
		# If odd, then yellow. First turn is yellow.
		if numTurns % 2:
			print("\nTurn " + str(numTurns) + " - " + p1.name + "'s turn")
			
			while True:
				columnOfChoice = int(input(p1.name + ", please choose which column to insert your disc: "))
				print("")
				# Because arrays start from 0, visually from 1.
				columnOfChoice -= 1
				
				isWithinBounds = 0 <= columnOfChoice <= board.col-1
				if isWithinBounds:
					isOverflow = columnOverflow(board, columnOfChoice)
				if not isWithinBounds:
					print("[Error] Please choose a column within 1 - " + str(board.col) + ".")
				elif isOverflow:
					print("[Error] Please choose a column that is not fully filled with discs.")
				if isWithinBounds and not isOverflow:
					break
				
			placeDisc(p1, board, columnOfChoice)
			
			if checkIfWin(p1, board):
				printBoard(p1, p2, board)
				return p1
		# else all is red's turn.
		else:
			print("\nTurn " + str(numTurns) + " - " + p2.name + "'s turn")
			
			while True:
				columnOfChoice = int(input(p2.name + ", please choose which column to insert your disc: "))
				print("")
				# Because arrays start from 0, visually from 1.
				columnOfChoice -= 1
				
				isWithinBounds = 0 <= columnOfChoice <= board.col-1
				if isWithinBounds:
					isOverflow = columnOverflow(board, columnOfChoice)
				if not isWithinBounds:
					print("[Error] Please choose a column within 1 - " + str(board.col) + ".")
				elif isOverflow:
					print("[Error] Please choose a column that is not fully filled with discs.")
				if isWithinBounds and not isOverflow:
					break
				
			placeDisc(p2, board, columnOfChoice)
			
			if checkIfWin(p2, board):
				printBoard(p1, p2, board)
				return p2
			
		numTurns += 1
		
		
# Function prints the end game result and shows who wins.
# It takes in the winning player's object.
def printEndGame(winningPlayer):
	print("Congratulations " + winningPlayer.name + ", you won the game.")


# This is the main function.
if __name__ == "__main__":
	# Step 1 - Init players and Board.
	p1 = Player(input("Enter player name that represents x (Yellow discs): "), "yellow")
	p2 = Player(input("Enter player name that represents o (Red discs): "), "red")
	board = Board()
	
	# Step 2 - Manage turns.
	winningPlayer = manageTurns(p1, p2, board)
	
	# Step 3 - Print end results.
	printEndGame(winningPlayer)
