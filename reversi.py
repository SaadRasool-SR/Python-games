"""
CMPUT 175 - Assignment 2 Template
"""

"""
Hints:
    - self.gameBoard represents the game board
    - self.playerColour represents the colour of the human player
    - self.computerColour represents the colour of the computer
    - the colour arguments are eiter self.WHITE or self.BLACK, which are defined below
"""

class Reversi:
    WHITE = "w "
    BLACK = "b "
    EMPTY = ". "
    SIZE = 8
    
# color could either be black = 'b' or white = 'w'
    def __init__(self,colour):
        self.newGame()
        self.colour = colour # Creating an instance of colour


    """
    Functionality:
        Create the game state so players can play again
    Parameters: 
        None
    """
    def newGame(self):
        self.gameBoard = [] # creating an empty list called gameboard 
        #Creating the Game Board, with initial colour tiles 
        for i in range(self.SIZE):
            self.gameBoard.append([self.EMPTY] * 8)
        self.gameBoard[3][3] = self.WHITE
        self.gameBoard[3][4] = self.BLACK
        self.gameBoard[4][3] = self.BLACK
        self.gameBoard[4][4] = self.WHITE
        return

    """
    Functionality:
        Return the score of the player
    Parameters:
        colour: The colour of the player to get the score for 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def getScore(self):
        score = {} # creating a dictionary for keeping score 
        b_score = 0 # initial score  = 0
        W_score = 0 
        # searching for white and black tiles and then incrementing score 
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if self.gameBoard[x][y] == self.WHITE:
                    W_score += 1
                elif self.gameBoard[x][y] == self.BLACK:
                    b_score += 1
        score['White'] = W_score # appending to dictionary 
        score['Black'] = b_score
        
        return score


    """
    Functionality:
        Set the colour for the human player to the designated colour, as well as the computer will have the other colour
    Parameters:
        colour: The colour of the player the user wants to play as 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def setPlayerColour(self, colour):  # setting colour for player and computer 
        if colour == self.WHITE:
            self.playerColour = self.WHITE
            self.computerColour = self.BLACK
        else:
            self.playerColour = self.BLACK
            self.computerColour = self.WHITE
            
        return self.computerColour
    

    """
    Functionality:
        Print out the current board state
        The index of the rows and columns should be on the left and top.
        See the sample output for details
    Parameters: 
        None
    """
    def displayBoard(self):
        # displaying game board  and score 
        print('  0  1  2  3  4  5  6  7')
        for y in range(self.SIZE):
            print('%s' %(y),end=' ')
            for x in range(self.SIZE):
                print(self.gameBoard[x][y], end=' ')
            print('')
        Score = self.getScore()
        print('Score: ' + 'white '+str(Score['White']) +',' +' black ' + str(Score['Black']))
        return


    """
    Functionality:
        Return true if the input position 'position' is valid for the given player 'colour' to make
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def isPositionValid(self, position, colour):
        x,y = position[0],position[1] # As position is a list, setting x and y variables 
        
        # checking if the position is on gameboard and the position is not already taken by a tile
        if not self.PositionOnBoard(x,y) or self.gameBoard[x][y] != self.EMPTY:
            return False 
        # defining colour and other colour to find out if its a valid move or not 
        if colour == self.WHITE:
            othercolour = self.BLACK

        elif colour == self.BLACK:
            othercolour = self.WHITE
        
        # setting direction that needs to be checked from the position, created a list of all the direction
        # for the position
        for xdirection, ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]: # moving in all direction
            x,y = position[0],position[1]
            x += xdirection # 1st step in x direction 
            y += ydirection # 1st step in y direction
            if self.PositionOnBoard(x,y) and self.gameBoard[x][y] == othercolour:  # if its a valid move
                x += xdirection # incrementing again 
                y += ydirection
                if not self.PositionOnBoard(x,y):
                    continue
                while self.gameBoard[x][y] == othercolour: # incrementing again to find our colour tile 
                    x += xdirection 
                    y += ydirection
                    if not self.PositionOnBoard(x,y): # if not on board than invalid position 
                        break
                if not self.PositionOnBoard(x,y):
                    continue
                if self.gameBoard[x][y] == colour: # if in the direction there is a tile with our colour than the move is valid 
                    return True
                
     # Created a method to check if the position is on the Game board            
    def PositionOnBoard(self, x, y):
        # Returns True if the position is located on the board 
        return x >= 0 and x <= self.SIZE - 1  and y >= 0 and y <= self.SIZE - 1  
        
            
    """
    Functionality:
        Return true if the game is over, false otherwise
        The game is over if any player cannot make a move, no matter whose turn it is
    Parameters: 
        None
    Note: 
        Skipping is not allowed
    """
    
    # Method to check if it the game is over 
    def isGameOver(self):
        if self.colour == self.WHITE:
            othercolour = self.BLACK
        elif self.colour == self.BLACK:
            othercolour = self.WHITE
            
        # if there are empty tiles and theres still a valid position valiable
        if self.getMoves(self.colour) != [] or self.getMoves(othercolour) != []:
            print(self.getMoves(self.colour))
            print(self.getMoves(othercolour))
            return False
        else:
            print(self.getMoves(self.colour))
            print(self.getMoves(othercolour))
            return True
        

        
    """
    Functionality:
        Make the given move for the human player, and capture any pieces
        If you assume the move is valid, make sure the validity is checked before calling
    Parameters: 
        position -> A list [i,j] where i is the row and j is the column
        colour: The colour that is making the move 
                Use BLACK or 'b' for black, WHITE or 'w' for white
    """
    def makeMovePlayer(self, position):
        x = position[0]
        y = position[1]
        
        if self.colour == self.WHITE:
            othercolour = self.BLACK
        elif self.colour == self.BLACK:
            othercolour = self.WHITE

            
        ToFlip = [] # creating an empty list for the tiles to flip 
        if self.isPositionValid(position, self.colour): # checks if the position is valid 
            for xdirection, ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]: # moving in all direction
                x += xdirection # 1st step in x direction 
                y += ydirection # 1st step in y direction
                while self.PositionOnBoard(x,y) and self.gameBoard[x][y] == othercolour:  # valid move
                    x += xdirection 
                    y += ydirection 
                    if self.PositionOnBoard(x,y) and self.gameBoard[x][y] == self.colour:
                        while True:
                            x -= xdirection # going in reverse until we return to the same position as we started as 
                            y -= ydirection # going in reverse until we return to the same position as we started as 
                            if x == position[0] and y == position[1]:
                                break
                            ToFlip.append([x,y])  # appending the tiles into the list until we reach the starting position
                x = position[0]
                y = position[1]
         
        # creating this for the computer of the othercolour tiles               
        if len(ToFlip) == 0:
            for xdirection, ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]: # moving in all direction
                x += xdirection # 1st step in x direction 
                y += ydirection # 1st step in y direction
                while self.PositionOnBoard(x,y) and self.gameBoard[x][y] == self.colour:  # valid move
                    x += xdirection 
                    y += ydirection 
                    if self.PositionOnBoard(x,y) and self.gameBoard[x][y] == othercolour:
                        while True:
                            x -= xdirection
                            y -= ydirection 
                            if x == position[0] and y == position[1]:
                                break
                            ToFlip.append([x,y])
                x = position[0]
                y = position[1]
                
        return ToFlip
        

    """
    Functionality:
        Make a naive move for the computer
        This is the first valid move when scanning the board left to right, starting at the top
    Parameters: 
        None
    """
    # this method calls getMoves method which generated random valid positions for the computer 
    # and the first position in the list is returned as a valid move 
    def makeMoveNaive(self):
        if self.colour == self.WHITE:
            othercolour = self.BLACK
        elif self.colour == self.BLACK:
            othercolour = self.WHITE
            
        random_moves = self.getMoves(othercolour)
        return random_moves[0] # first valid move is returned 

    """
    Functionality:
        Make a move for the computer which is the best move available
        This should be the move that results in the best score for the computer
    Parameters: 
        None
    """
    # the main methodology used in this method is that, from the valid moves for the getMoves method, 
    # the move with the highest number of tiles to flip 
    # will be used as a smart position
    # also is there is a corner move avaliable
    # the computer will always try to go for a corner move first and check if its valiable 
    def makeMoveSmart(self):
        # list of all possible moves 
        if self.colour ==  self.WHITE:
            othercolour = self.BLACK
        else:
            othercolour = self.WHITE
            self.colour = self.BLACK
        position = self.getMoves(othercolour)
                
        for i in range(len(position)):
            if self.isOnCorner(position[i]):
                return position[i]
        
        bestscore = 0
        j = 0
        for x,y in position:
            dupeBoard = self.getBoardcopy()
            for xdirection, ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
                x = position[j][0]
                y = position[j][1]
                x += xdirection
                y += ydirection
                if self.PositionOnBoard(x,y) and dupeBoard[x][y] == self.colour:
                    x += xdirection
                    y += ydirection
                    if not self.PositionOnBoard(x,y):
                        continue
                    while dupeBoard[x][y] == self.colour:
                        x += xdirection
                        y += ydirection
                        if not self.PositionOnBoard(x,y):
                            break
                    if not self.PositionOnBoard(x,y):
                        continue
                    if dupeBoard[x][y] == othercolour:
                        t = 0
                        while True:
                            x-= xdirection
                            y-= ydirection
                            if x == position[j][0] and y == position[j][1]:
                                break
                            t+=1
                            if t > bestscore:
                                bestscore = t
                                bestmove = [position[j][0],position[j][1]]
            j += 1  
        return bestmove
    
    # checks if there is a corner move avaliable 
    def isOnCorner(self,position):
        x = position[0]
        y = position[1]
        return (x == 0 or y == 0) or  (x == 7 or y == 0) or (x == 0 or y == 7) or  (x == 7 or y == 7)
 
    # get random valid moves 
    def getMoves(self,color):
        getValidMoves = []
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                position = [x,y]
                if self.isPositionValid(position,color) == True:
                    getValidMoves.append(position)                    
        return getValidMoves
    
    
    # creates a copy of the board which is used by the computer to calculate which move has 
    # the most number of tiles being flipped 
    def getBoardcopy(self):
        duplicateBoard = self.gameBoard
        #for x in range(self.SIZE):
         #   for y in range(self.SIZE):
          #      duplicateBoard[x][y] = self.gameBoard[x][y]
        return duplicateBoard
    
    # method that updates the board 
    def update(self,position,colour):
        j = position[0]
        k = position[1]
        To_Flip = self.makeMovePlayer(position)
        for i in range(len(To_Flip)):
            x = To_Flip[i][0]
            y = To_Flip[i][1]
            self.gameBoard[x][y] = colour
        self.gameBoard[j][k] = colour   