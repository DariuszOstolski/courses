# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        Creates a rat positioned at given row and col
        
        >>> rat = Rat('P', 0, 0)
        >>> rat.symbol
        P
        >>> rat.num_sprouts_eaten
        0
        >>> rat.row
        0
        >>> rat.col
        0
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
        
    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Sets rat at given position
        
        >>> rat = Rat('P', 0, 0)
        >>> rat.set_location(1,2)
        >>> rat.row
        1
        >>> rat.col
        2
        """
        self.row = row
        self.col = col
        
    def eat_sprout(self):
        """ (Rat) -> NoneType

        Adds one eaten brussels sprout
        
        >>> rat = Rat('P', 0, 0)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        2
        """
        self.num_sprouts_eaten += 1
        
    def __str__(self):
        """ (Rat) -> str

        Returns string description of a rat

        >>> rat = Rat('P', 4, 3)
        >>> str(rat)
        P at (4, 3) ate 0 sprouts.
        """
        return '%s at (%d, %d) ate %d sprouts.'%(self.symbol, self.row, self.col, self.num_sprouts_eaten)
    
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        Creates a Maze with 2 rats
            
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = self.__count_sprouts_left()
        
    def __count_sprouts_left(self):
        """  (Maze) -> Int

        Counts left sprouts in a maze
        
        """
        num_sprouts = 0
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.get_character(row, col) == SPROUT:
                    num_sprouts += 1
        return num_sprouts
    
    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Return True if and only if there is a wall at the
        given row and column of the maze.
        
        """
        return (self.get_character(row, col) == WALL)

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Returns character at given row and col
        
        """
        character = self.maze[row][col]
        if self.__check_rat_position(self.rat_1, row, col):
            character = self.rat_1.symbol
        elif self.__check_rat_position(self.rat_2, row, col):
            character = self.rat_2.symbol
        return character

    def __get_row_after_move(self, rat, vdirection):
        """ (Maze, Rat, int) -> int

        Returns new row after move to given direction
        """
        return rat.row+vdirection

    def __get_col_after_move(self, rat, hdirection):
        """ (Maze, Rat, int) -> int

        Returns new col after move to given direction
        """        
        return rat.col+hdirection
        
    def move(self, rat, vdirection, hdirection):
        """ (Maze, Rat, int, int) -> bool

        Move the rat in the given direction, unless there is a wall in the way.

        Also, check for a Brussels sprout at that location and, if present:

        - have the rat eat the Brussels sprout,
        - make that location a HALL, and
        - decrease the value that num_sprouts_left refers to by one.

        """
        row = self.__get_row_after_move(rat, vdirection)
        col = self.__get_col_after_move(rat, hdirection)
        if self.is_wall(row, col):
            return False
        
        if self.get_character(row, col)==SPROUT:
            self.maze[row][col] = HALL
            rat.eat_sprout()            
            self.num_sprouts_left -= 1
            
        rat.set_location(row, col)
        return True
    
    def __check_rat_position(self, rat, row, col):
        """ (Maze, Rat, int, int) -> bool

        Check if Rat 
        """
        return (rat.row==row and rat.col==col)
    
    def __str__(self):
        """ (Maze) -> str

        Return a string representation of the maze
        
        """
        maze = ''
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.__check_rat_position(self.rat_1, row, col):
                    maze += self.rat_1.symbol
                elif self.__check_rat_position(self.rat_2, row, col):
                    maze += self.rat_2.symbol
                else:
                    maze += self.maze[row][col]
            maze += '\n'
        maze += str(self.rat_1)+'\n'
        maze += str(self.rat_2)
        return maze
    
