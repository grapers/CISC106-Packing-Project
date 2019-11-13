class Grid:
    """ Has attributes numRows, numCols, and squares (a 2D list containing True/False). """
    def __init__(self,rows,cols,squares):
        self.numRows = rows
        self.numCols = cols
        self.squares = squares if squares else [cols * [False] for r in range(rows)]
        
    def updateGrid(self, shape):
        """ Top-level def for placing a single shape on grid. Finds best position and rotation for shape,
        update grid squares (mutates). Calls: find_max_score_location Returns boolean: fits or not
        """
        
    def print(self):
        """ Print the grid, using an asterisk for each true square, underscore for false.
        Use a newline after each row, and no spaces in rows.
        """
        for row in range(self.numRows):
            for boolean in self.Squares[row]:
                if boolean: #if True
                    print("*", end ="")
                else: #if False
                    print("_", end = "")
            print("\n")