data = []

with open("AdventOfCode\\2021\\4\\input.txt","r") as f:
    data = f.readlines()

def mark_in_board(board, num):
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j][0] == num:
                board[i][j][1] = True

def check_win(board):
    m, n = len(board), len(board[0])
    for i in range(m):
        if sum(item[1] for item in board[i]) == n:
            return True

    transpose_board = list(zip(*board))
    for j in range(n):
        if sum(item[1] for item in transpose_board[j]) == m:
            return True

    return False

def get_score(board):
    m, n = len(board), len(board[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if not board[i][j][1]:
                ans += board[i][j][0]

    return ans

def solve(data):
    nums = list(map(int, data[0].split(",")))
    boards = []
    board = None
    for line in data[1:]:
        if len(line) == 1:
            boards.append(board)
            board = []
        else:
            line_nums = list(map(int, line.split()))
            board.append([[line_num, False] for line_num in line_nums])

    boards = boards[1:]  #first one is a None board

    for num in nums:
        for board in boards:
            mark_in_board(board, num)
            if check_win(board):
                return get_score(board) * num

    return 0

print(solve(data))

