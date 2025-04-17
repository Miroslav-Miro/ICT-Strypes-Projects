from typing import Dict, Optional

# Global variables
GAME_RUNNING: bool = True
counter: int = 0

# Board type
Board = Dict[str, Optional[str]]

# Initialize empty board
board: Board = {
    '1,1': None, '1,2': None, '1,3': None,
    '2,1': None, '2,2': None, '2,3': None,
    '3,1': None, '3,2': None, '3,3': None
}

def print_board(e_b: Board) -> None:
    """
    Prints the current state of the Tic-Tac-Toe board.
    :param e_b: A dictionary representing the game board.
    :type e_b: Board
    """
    for row in range(1, 4):
        print(f"{e_b[f'{row},1'] or ' '} | {e_b[f'{row},2'] or ' '} | {e_b[f'{row},3'] or ' '}")
        if row < 3:
            print("---------")


def is_there_a_winner(board: Board) -> bool:
    """
    Checks if there's a winner and prints the winner symbol.
    :param board: A dictionary representing the game board.
    :return: False if there is a winner, otherwise True to continue the game.
    """
    if winner(board):
        if counter % 2 == 0:
            print('----X wins----')
        else:
            print('----O wins----')
        return False
    return True


def winner(e_b: Board) -> bool:
    """
    Determines whether there is a winner on the current board.
    :param e_b: A dictionary representing the game board.
    :return: True if a player has won, False otherwise.
    """
    if e_b['1,1'] is e_b['1,2'] is e_b['1,3'] is not None:
        is_winner = True
    elif e_b['1,1'] is e_b['2,2'] is e_b['3,3'] is not None:
        is_winner = True
    elif e_b['2,1'] is e_b['2,2'] is e_b['2,3'] is not None:
        is_winner = True
    elif e_b['3,1'] is e_b['3,2'] is e_b['3,3'] is not None:
        is_winner = True
    elif e_b['1,1'] is e_b['2,1'] is e_b['3,1'] is not None:
        is_winner = True
    elif e_b['1,2'] is e_b['2,2'] is e_b['3,2'] is not None:
        is_winner = True
    elif e_b['1,3'] is e_b['2,3'] is e_b['3,3'] is not None:
        is_winner = True
    elif e_b['3,1'] is e_b['2,2'] is e_b['1,3'] is not None:
        is_winner = True
    else:
        is_winner = False

    return is_winner


def whose_turn_it_is() -> str:
    """
    Prompts the current player (X or O) to enter their move.
    :return: The user's input representing their move.
    """
    if counter == 0 or counter % 2 == 0:
        return input("O enters a move: ")
    else:
        return input("X enters a move: ")


# Game loop
while GAME_RUNNING and counter < 9:

    move: str = whose_turn_it_is()

    if move in board.keys():
        if board[move] is None:
            if counter % 2 == 0 or counter == 0:
                board[move] = 'O'
                counter += 1
            elif counter % 3 == 0 or counter == 1:
                board[move] = 'X'
                counter += 1
            elif counter == 9:
                print('DRAW')
                GAME_RUNNING = False
        else:
            print('Occupied')
    else:
        print('Invalid move')
        continue

    print_board(board)

    GAME_RUNNING = is_there_a_winner(board)
