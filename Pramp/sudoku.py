def isValid(board):
    #check if all rows are valid
    for i in range(0, 9):
        row_dups = set()
        col_dups = set()
        for j in range(0, 9):
            if board[i][j] != ".":
                if board[i][j] not in row_dups:
                    row_dups.add(board[i][j])
                else:
                    return False
                if board[i][j] not in col_dups:
                    col_dups.add(board[i][j])
                else:
                    return False
    #check if boxes are valid
    for r in range(0, 3):
        box_dups = set()
        for c in range(0, 3):
            if board[r][c] != ".":
                if board[r][c] not in box_dups:
                    box_dups.add(board[r][c])
                else:
                    return False

    #check if all cols are valid



def sudoku_solve(board):
    r,c = getEmptySpaces(board)
    if r == c == -1:
       return True
    for num in range(1, 10):
        if rowChecker(r, str(num), board) and colChecker(c, str(num), board) and boxChecker(r, c, str(num), board) :
            board[r][c] =  str(num)
            if sudoku_solve(board):
                return True
            board[r][c] = "."
    return False

def getEmptySpaces(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                return i, j
    return -1, -1

def rowChecker(r, num, board):
    for j in range(0, 9):
        if board[r][j] == num:
            return False
    return True


def colChecker(c, num, board):
    for j in range(0, 9):
        if board[j][c] == num:
            return False
    return True


def boxChecker(r, c, num, board):
    #other formula is r_start = r- r%3
    r_start = (r // 3) * 3
    r_end = r_start + 2
    c_start = (c // 3) * 3
    c_end = c_start + 2
    for i in range(r_start, r_end + 1):
        for j in range(c_start, c_end + 1):
            if board[i][j] == num:
                return False
    return True



board = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]

board1 = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]

print(sudoku_solve(board1))