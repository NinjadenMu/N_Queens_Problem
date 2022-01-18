
def check_if_attacking(q1, q2): #Check if queen 1 and queen 2 (q1 and q2) represented as coords are attacking each other, queens are last 2 queens placed by backtracking algorithm
    if q1[1] == q2[1]: #Check for columns (rows don't need to be checked since backtracking algorithm increases row once each iteration guaranteeing no 2 queens on same row)
        return True

    elif abs(q1[1] - q2[1]) == abs(q1[0] - q2[0]): #Check for diags
        return True

def find_num_sols(board, row_num): #brute force to get all sols
    if len(board) == 1:
        return 1

    elif row_num == len(board): #if last row completed (meaning all queens placed) and last 2 queens not attacking each other, then it is a valid sol
        for i in range(2, row_num + 1): #check every row from row_num - 2 to 0
            if check_if_attacking((row_num - i, board[row_num - i].index(1)), (row_num - 1, board[row_num - 1].index(1))):
                return 0

        return 1

    elif row_num > 1: #if at least 2 rows placed, check if queens attacking each other
        for i in range(2, row_num + 1): #check every row from row_num - 2 to 0
            if check_if_attacking((row_num - i, board[row_num - i].index(1)), (row_num - 1, board[row_num - 1].index(1))):
                return 0

    num_sols = 0
    for i in range(len(board)): #for every column
        board[row_num][i] = 1 #make that row, column 1
        num_sols += find_num_sols(board, row_num + 1) #find number of sols from new state
        board[row_num][i] = 0 #undo last action

    return num_sols

def find_one_sol_backtracking(board, row_num): #backtracking algorithm to find one solution
    if len(board) == 1:
        return [[1]]

    elif row_num > 1: #if at least 2 rows placed, check if queens attacking each other
        for i in range(2, row_num + 1): #check every row from row_num - 2 to 0 against the last row placed, not all queens have to be checked since previous queens guaranteed to be valid
            if check_if_attacking((row_num - i, board[row_num - i].index(1)), (row_num - 1, board[row_num - 1].index(1))):
                return False

        if row_num == len(board): #If all queens placed return valid board
            return board

    for i in range(len(board)):
        board[row_num][i] = 1 #try new queen placement on given row
        sol = find_one_sol_backtracking(board, row_num + 1) 
        if sol:
            return sol

        else: #if invalid undo and retry
            board[row_num][i] = 0

    

num_queens = int(input('How many queens should be placed?  This is also the dimension of the chess board: '))
print(find_one_sol_backtracking([[0 for i in range(num_queens)] for j in range(num_queens)], 0))

