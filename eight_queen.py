N = 8
counter = 0


def print_solution(chess_board):
    for row in range(N):
        for col in range(N):
            if chess_board[row] != col:
                print('-', end=' ')
            else:
                print('X', end=' ')
        print('\n')
    print('\n')


def isplaceok(chess_board, row, col):
    return not any(
        (chess_board[i] == col) or (chess_board[i] - col == row - i) or (chess_board[i] - col == i - row) for i in
        range(row))


def add_queen(chess_board, row):
    global counter
    if row >= N:
        print_solution(chess_board)
        counter += 1
    else:
        for col in range(N):
            if isplaceok(chess_board, row, col):
                chess_board[row] = col
                add_queen(chess_board, row + 1)


if __name__ == "__main__":
    chess_board = [-1] * N
    add_queen(chess_board, 0)
    print(counter)
