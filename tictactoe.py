import pygame
import random 
import time
from enum import Enum
pygame.init()

edge_width = 30
square_size = 120
gap = 5
square_color = (0, 128, 255)
draw_size = 46

# The flag that indicates if it is a user's turn or the computer's turn
UserTurn = True

class State(Enum):
	BLANK = -1
	O = 0
	X = 1
	
moves = [State.BLANK, State.BLANK, State.BLANK, State.BLANK,
		State.BLANK, State.BLANK, State.BLANK, State.BLANK,State.BLANK]

screen = pygame.display.set_mode((edge_width * 2 + square_size * 3 + gap * 2, edge_width * 2 + square_size * 3 + gap * 2))
pygame.display.set_caption('Tic Tac Toe') 

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score:', True, (128,0,0), (0, 128, 0))
textRect = text.get_rect() 
textRect.center = (edge_width + 2 * square_size + 2 * gap, edge_width / 2) 

# Play music
pygame.mixer.music.load('fusion_of_dhol.mp3')
pygame.mixer.music.play(-1)

# Function to draw an O or an X on a given square that is specified by row number and column number
def drawOX(row_num, col_num, state):
	print ("Drawing image for row " + str(row_num) + " and column " + str(col_num))
	x_coord = edge_width + (col_num-1)*square_size + square_size/2 + (col_num - 1)*gap - draw_size/2
	y_coord = edge_width + (row_num-1)*square_size + square_size/2 + (row_num - 1)*gap - draw_size/2
	print ("Coordinates are x = " + str(x_coord) + " y = " + str(y_coord))
	if(state == State.X):
		pygame.draw.line(screen, (0, 0, 0), (x_coord, y_coord), (x_coord + draw_size, y_coord + draw_size), 5)
		pygame.draw.line(screen, (0, 0, 0), (x_coord + draw_size, y_coord), (x_coord, y_coord + draw_size), 5)
	elif(state == State.O):
		pygame.draw.circle(screen, (0, 0, 0), (int(x_coord + draw_size/2), int(y_coord + draw_size/2)), int(draw_size/2), 4)
	pygame.display.update()

def checkForWin():
	print (moves)
	if(moves[0] == moves[3] and moves[0] == moves[6] and moves[0] != State.BLANK):
		print("Win detected - First Column!")
		pygame.draw.line(screen, (128, 0, 0), (int(edge_width+square_size/2),int(edge_width+square_size/2)),
			(int(edge_width+square_size/2), int(edge_width+5*square_size/2+2*gap)), 4)
		pygame.display.update()
		return moves[0]
	if(moves[1] == moves[4] and moves[1] == moves[7] and moves[1] != State.BLANK):
		print("Win detected! - Second Column")
		pygame.draw.line(screen, (128, 0, 0), (int(edge_width+3*square_size/2+gap),int(edge_width+square_size/2)),
			(int(edge_width+3*square_size/2+gap), int(edge_width+5*square_size/2+2*gap)), 4)
		pygame.display.update()
		return moves[1]	  
	if(moves[2] == moves[5] and moves[2] == moves[8] and moves[2] != State.BLANK):
		print("Win detected! - Third Column")
		pygame.draw.line(screen, (128, 0, 0), (int(edge_width+5*square_size/2+2*gap),int(edge_width+square_size/2)),
			(int(edge_width+5*square_size/2+2*gap), int(edge_width+5*square_size/2+2*gap)), 4)
		pygame.display.update()
		return moves[2]
	if(moves[0] == moves[1] and moves[0] == moves[2] and moves[0] != State.BLANK):
		print("Win detected! - First Row")
		pygame.draw.line(screen, (128, 0, 0), (int(edge_width + square_size/2),int(edge_width + square_size/2)),
			(int(edge_width + 5*square_size/2 + 2*gap), int(edge_width + square_size/2)), 4)
		pygame.display.update()
		return moves[0]
	if(moves[3] == moves[4] and moves[3] == moves[5] and moves[3] != State.BLANK):
		print("Win detected! - Second Row")
		pygame.draw.line(screen, (128, 0, 0), (int(edge_width + square_size/2),int(edge_width + 3*square_size/2 + gap)),
			(int(edge_width + 5*square_size/2 + 2*gap), int(edge_width + 3*square_size/2 + gap)), 4)
		pygame.display.update()
		return moves[3]
	if(moves[6] == moves[7] and moves[6] == moves[8] and moves[6] != State.BLANK):
		print("Win detected! - Third Row")
		pygame.draw.line(screen, (128, 0, 0), (int(edge_width + square_size/2),int(edge_width + 5*square_size/2 + 2*gap)),
			(int(edge_width + 5*square_size/2 + 2*gap), int(edge_width + 5*square_size/2 + 2*gap)), 4)
		pygame.display.update()
		return moves[6]
	if(moves[0] == moves[4] and moves[0] == moves[8] and moves[0] != State.BLANK):
		print("Win detected! - Backslash (\)")
		pygame.draw.line(screen, (128, 0, 0), (int(edge_width + square_size/2),int(edge_width + square_size/2)),
			(int(edge_width + 5*square_size/2 + 2*gap), int(edge_width + 5*square_size/2 + 2*gap)), 4)
		pygame.display.update()
		return moves[0]
	if(moves[2] == moves[4] and moves[2] == moves[6] and moves[2] != State.BLANK):
		print("Win detected! - Slash (/)")
		pygame.draw.line(screen, (128, 0, 0), (int(edge_width + 5*square_size/2 + 2*gap),int(edge_width + square_size/2)),
			(int(edge_width + square_size/2), int(edge_width + 5*square_size/2 + 2*gap)), 4)
		pygame.display.update()
		return moves[2]
	print ("No win yet")
	return State.BLANK

# Check for the end of the game
def checkForEnd():
	for i in moves:
		if(i == State.BLANK):
			return False;
	return True;

def flushGame():
	i = 0
	while i < 9:
		moves[i] = State.BLANK
		i += 1
	UserTurn = True
	drawTicTacToe()
	pygame.event.clear()

# Computer moves. Randomly.
def computer_move():
	print ("Computer playing")
	played = False
	while (played == False):
		# Pick a random number, and check if it is a blank
		randnum = random.randrange(1, 9)
		print ("Checking if " + str(randnum) + " has been played")
		if(moves[randnum-1] == State.BLANK):
			print (str(randnum) + " is blank. Playing...")
			if(randnum == 1 or randnum == 4 or randnum == 7):
				col_num = 1
			elif(randnum == 2 or randnum == 5 or randnum == 8):
				col_num = 2
			elif(randnum == 3 or randnum == 6 or randnum == 9):
				col_num = 3
			if(randnum == 1 or randnum == 2 or randnum == 3):
				row_num = 1
			elif(randnum == 4 or randnum == 5 or randnum == 6):
				row_num = 2
			elif(randnum == 7 or randnum == 8 or randnum == 9):
				row_num = 3
			print ("Drawing in " + str(row_num) + " and " + str(col_num))
			drawOX(row_num, col_num, State.O)
			played = True
			moves[randnum-1] = State.O
			print ("Wrote 0 - computer move - for " + str(randnum-1))
		
	
# Draw the Tic Tac Toe
def drawTicTacToe():
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 2*edge_width+3*square_size+2*gap, 2*edge_width+3*square_size+2*gap))
	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width, edge_width, square_size, square_size))
	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width, edge_width + square_size + gap, square_size, square_size))
	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width, edge_width + square_size*2 + gap*2, square_size, square_size))

	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width + square_size + gap, edge_width, square_size, square_size))
	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width + square_size + gap, edge_width + square_size + gap, square_size, square_size))
	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width + square_size + gap, edge_width + square_size*2 + gap*2, square_size, square_size))
	
	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width + square_size*2 + gap*2, edge_width, square_size, square_size))
	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width + square_size*2 + gap*2, edge_width + square_size + gap, square_size, square_size))
	pygame.draw.rect(screen, square_color, pygame.Rect(edge_width + square_size*2 + gap*2, edge_width + square_size*2 + gap*2, square_size, square_size))
	pygame.display.flip()
	
row = 0
column = 0
drawTicTacToe()
done = False
while done == False:
	if(UserTurn == True):
		#print ("UserTurn is " + str(UserTurn))
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):				 # If user wants to quit
				done = True
			if(event.type == pygame.MOUSEBUTTONDOWN):		# if user clicks on a square
				Mouse_x, Mouse_y = pygame.mouse.get_pos()
				print ("Captured mouse event " + str(Mouse_x) + " " + str(Mouse_y))
				if(Mouse_x > edge_width and Mouse_x < (edge_width + square_size)):
					column = 1
				elif(Mouse_x > (edge_width + square_size + gap) and Mouse_x < (edge_width + square_size*2 + gap)):
					column = 2
				elif(Mouse_x > (edge_width + square_size*2 + gap*2) and Mouse_x < (edge_width + square_size*3 + gap*2)):
					column = 3
				if(Mouse_y > edge_width and Mouse_y < (edge_width + square_size)):
					row = 1
				elif(Mouse_y > (edge_width + square_size + gap) and Mouse_y < (edge_width + square_size*2 + gap)):
					row = 2
				elif(Mouse_y > (edge_width + square_size*2 + gap*2) and Mouse_y < (edge_width + square_size*3 + gap*2)):
					row = 3
			
				print ("Row and Column with the click are " + str(row) + " " + str(column))
				# User Move. Record this move only if the block is empty
				if(column > 0 and column < 4 and row > 0 and row < 4 and moves[(row - 1) * 3 + column - 1] == State.BLANK):
					drawOX(row, column, State.X)
					moves[(row - 1) * 3 + column - 1] = State.X
					UserTurn = False
					print ("Move completed. UserTurn is " + str(UserTurn))
					if(checkForWin() == State.X):
						print ("You win!")
						#pygame.mixer.music.load('Battle_Crowd_Celebration.mp3')
						#pygame.mixer.music.play(0)
						time.sleep(10)
						flushGame()						   # Refresh the board  
						UserTurn = True
					if(checkForEnd() == True):
						print("It's a draw!")
						time.sleep(5)
						flushGame()							# Refresh the board
						UserTurn = True
	else:
		# After the user move, computer moves, after waiting
		if(UserTurn == False and done == False):
			print ("Computer's turn. UserTurn is " + str(UserTurn))
			time.sleep(1)
			computer_move()
			if(checkForWin() != State.BLANK):
				# Play sounds
				# Draw line
				print("Computer wins!")
				#pygame.mixer.music.load('Battle_Crowd_Celebration.mp3')
				#pygame.mixer.music.play(0)
				time.sleep(10)
				flushGame()
				UserTurn = True
			elif(checkForEnd() == True):
				print("It's a draw!")
				time.sleep(5)
				flushGame()		
				UserTurn = True
			else:
				UserTurn = True
		
