class Shape:
    """ A "shape" is a nested tuple, where the real world shape is represented as ones.
    For example, an "L" shape could be represented as
    ((False, False, True),(True, True, True))
    Has attributes x, y, letter, squares (a nested list of type boolean), color, num_rotations
    """
    def __init__(self, letter, squares, color):
        self.x = 0 # will be modified later to indicate position
        self.y = 0 # will be modified later to indicate position
        self.letter = letter
        self.squares = squares
        self.color = color
        self.num_rotations = 0
        
    def rotate90(self):
        """ Rotates this shape 90 degrees clockwise (direction matters).
        Mutates squares and num_rotations Returns None
        """
        
    def generate_all_locations(grid, shape):
        """ Takes a single shape in one position and finds all the places
        it could fit on the grid, given its dimensions. Returns: a list of row,col tuples
        """
        
    def get_valid_locations(location_list, grid, shape):
        """ Returns list of locations where shape does not overlap shapes already on grid.
        Assumes that all locations in parameter list are potential fits for this shape.
        Calls: fits
        """
        
    def fits(location, grid, shape):
        """ Returns True if shape placed at location does not overlap shapes already on grid.
        location: row,col tuple
        """
        
    def get_max_score(location_list, grid, shape):
        """ Finds highest scoring location from list, given shape.
        When scores are equal, the lowest row (highest row number), right end (highest column) should be preferred.
        Return: nested tuple of (location_tuple,number) Calls: get_score
        """
        
    def get_score(location, grid, shape):
        """ Computes the score for a shape placed at a single location on grid.
        Scores are positive, higher is better. For now, code the heuristic discussed in class.
        location: row,col tuple Returns: number
        """
        
    def find_max_score_location(grid, shape):
        """ Takes a single shape, finds best position on grid.
        Tries original and three possible 90 degree rotations.
        Mutates shape for each rotation. When scores are equal,
        the lowest row (highest row number), right end (highest column) should be preferred.
        Returns tuple: (fits numberRotations location) fits: bool maxScoreRow, maxScoreCol: upper left coordinates of best position
        for shape on grid numberRotations: 0-3 rotations required for best fit.
        Calls: rotate90, generate_all_locations, get_valid_locations, get_max_score
        """
        
    def get_shape(letter):
        """ Returns the Shape corresponding to the letter parameter:
        I for a line; T for a T; L for an L on its back, foot to right; Z for a Z.
        More may be added.
        """
        if letter == "I":
            return ((True,True,True,True))
        elif letter == "T":
            return ((False,True,False),(True,True,True))
        elif letter == "L":
            return ((False,False,True),(True,True,True))
        elif letter == "Z":
            return ((True,True,False),(False,True,True))