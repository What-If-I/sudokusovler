# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.


def grid_indexes():
    for x in range(0, 9):
        for y in range(0, 9):
            yield x, y


# TODO: set() on cell should return only value
class Cell(object):

    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.square = self.calc_square(x, y)

    def __set__(self, instance, value):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.value == other.value
        return self.value == other

    def __cmp__(self, other):
        if isinstance(other, Cell):
            return cmp(self.value, other.value)
        return cmp(self.value, other)

    @staticmethod
    def calc_square(x, y):
        return x / 3, y / 3

    def __str__(self):
        return self.value

    def __repr__(self):
        return "<Cell> {} at {}, {} sqr:{}".format(self.value, self.x, self.y, self.square)


class Grid(object):

    def __init__(self, lst):
        self.cells = []
        for x, row in enumerate(lst):
            for y, value in enumerate(row):
                self.cells.append(Cell(value, x, y))

    def __iter__(self):
        for cell in self.cells:
            yield cell

    def row(self, x):
        assert x < 9
        row_start = x * 8
        return self.cells[row_start:row_start + 9]

    def column(self, y):
        assert y < 9
        return self.cells[y::9]

    def square(self, sqr):
        assert sqr < 9
        return [cell for cell in self.cells if cell.square == sqr]

# solve_sudoku should return None
ill_formed = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9],  # <---
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# solve_sudoku should return valid unchanged
valid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# solve_sudoku should return False
invalid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
           [6, 7, 2, 1, 9, 5, 3, 4, 8],
           [1, 9, 8, 3, 8, 2, 5, 6, 7],
           [8, 5, 9, 7, 6, 1, 4, 2, 3],
           [4, 2, 6, 8, 5, 3, 7, 9, 1],
           [7, 1, 3, 9, 2, 4, 8, 5, 6],
           [9, 6, 1, 5, 3, 7, 2, 8, 4],
           [2, 8, 7, 4, 1, 9, 6, 3, 5],
           [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2, 9, 0, 0, 0, 0, 0, 7, 0],
        [3, 0, 6, 0, 0, 8, 4, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 0, 2],
        [0, 2, 0, 0, 3, 1, 0, 0, 7],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [1, 0, 0, 9, 5, 0, 0, 6, 0],
        [7, 0, 0, 0, 9, 0, 0, 0, 1],
        [0, 0, 1, 2, 0, 0, 3, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 5, 9]]


# Note: this may timeout
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
#
# hard = [[1,0,0,0,0,7,0,9,0],
#         [0,3,0,0,2,0,0,0,8],
#         [0,0,9,6,0,0,5,0,0],
#         [0,0,5,3,0,0,9,0,0],
#         [0,1,0,0,8,0,0,0,2],
#         [6,0,0,0,0,4,0,0,0],
#         [3,0,0,0,0,0,0,1,0],
#         [0,4,0,0,0,0,0,0,7],
#         [0,0,7,0,0,0,3,0,0]]

def get_elem_square(x, y, grid):
    x = (int(x / 3) * 3)
    y = (int(y / 3) * 3)
    square = []
    for row in range(x, x + 3):
        for col in range(y, y + 3):
            square.append(grid[row][col])
    return square


def find_known_numbers(cell, grid):
    square = grid.square(cell.square)
    row = grid.row(cell.x)
    col = grid.column(cell.y)
    return set(square + row + col) - {0}


def get_column(grid, y):
    return list(tuple((zip(*grid)))[y])


def assume_numbers(grid):
    guessed_grid = Grid(grid)
    for cell in guessed_grid:
        if cell == 0:
            known_numbers = find_known_numbers(cell, guessed_grid)
            guess = set(range(1, 10)) - known_numbers
            cell.value = guess

    # for x, y in grid_indexes():
    #     cell = guessed_grid[x][y]
    #     if isinstance(cell, set):
    #         find_equal_set(cell, guessed_grid[x])

    return guessed_grid


def find_equal_set(cell, guessed_grid):
    for y1, c1 in enumerate(guessed_grid):
        if cell == c1:
            return y1


def compare_with_list(compare, with_list, position):
    superset = set()
    for val in with_list:
        if isinstance(val, set):
            superset = superset | val
    return superset - compare


def solve_sudoku(grid):
    found_one = True
    solved = False

    while found_one and not solved:
        found_one = False
        solved = True
        assummed_grid = assume_numbers(grid)

        for cell in assummed_grid:
            if isinstance(cell.value, set):
                solved = False

                guess = assummed_grid[x][y]
                if len(guess) == 1:
                    grid[x][y] = guess.pop()
                    found_one = True

    return grid


from pprint import pprint

# assert get_elem_square(8, 8, easy) == [0, 0, 1, 3, 0, 6, 0, 5, 9]
pprint(easy)
for row in solve_sudoku(easy):
    print(row)

    # print({1,2,3,} | {2,4,5})
