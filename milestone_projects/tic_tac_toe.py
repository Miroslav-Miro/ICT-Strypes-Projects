from typing import Dict, Optional, List, Union

# Global variables representing players
PLAYER_X: str = "X"
PLAYER_O: str = "O"

# Type alias for the game board
Board = Dict[str, Optional[str]]

# Initialize empty board with positions as keys
board: Board = {
    "1,1": None,
    "1,2": None,
    "1,3": None,
    "2,1": None,
    "2,2": None,
    "2,3": None,
    "3,1": None,
    "3,2": None,
    "3,3": None,
}


def print_board(board: Board) -> None:
    """
    Prints the current state of the Tic-Tac-Toe board.

    :param board: A dictionary representing the game board.
    """
    for row in range(1, 4):
        # Print each row, showing a space if the cell is empty
        print(
            f"{board[f'{row},1'] or ' '} | {board[f'{row},2'] or ' '} | {board[f'{row},3'] or ' '}"
        )
        if row < 3:
            print("---------")


def is_there_a_winner(board: Board, counter: int) -> List[Union[bool, str]]:
    """
    Checks if there's a winner and returns the game state.

    :param board: A dictionary representing the game board.
    :param counter: The number of turns played so far.
    :return: A list containing a boolean (True to continue, False if there's a winner),
             and optionally the winner message.
    """
    winner_print = ""
    is_it_still_playing = True

    # Check if there's a winner
    if winner(board):
        if counter % 2 == 0:
            winner_print = f"----{PLAYER_X} wins----"
        else:
            winner_print = f"----{PLAYER_O} wins----"
        is_it_still_playing = False

    # Return game status and winner message if game ended
    if is_it_still_playing:
        return [is_it_still_playing]

    return [is_it_still_playing, winner_print]


def winner(board: Board) -> bool:
    """
    Determines whether there is a winner on the current board.

    :param board: A dictionary representing the game board.
    :return: True if a player has won, False otherwise.
    """
    # Check all winning conditions
    if board["1,1"] is board["1,2"] is board["1,3"] is not None:
        is_winner = True
    elif board["1,1"] is board["2,2"] is board["3,3"] is not None:
        is_winner = True
    elif board["2,1"] is board["2,2"] is board["2,3"] is not None:
        is_winner = True
    elif board["3,1"] is board["3,2"] is board["3,3"] is not None:
        is_winner = True
    elif board["1,1"] is board["2,1"] is board["3,1"] is not None:
        is_winner = True
    elif board["1,2"] is board["2,2"] is board["3,2"] is not None:
        is_winner = True
    elif board["1,3"] is board["2,3"] is board["3,3"] is not None:
        is_winner = True
    elif board["3,1"] is board["2,2"] is board["1,3"] is not None:
        is_winner = True
    else:
        is_winner = False

    return is_winner


def whose_turn_it_is(counter: int) -> str:
    """
    Prompts the current player (X or O) to enter their move.

    :param counter: The current move count.
    :return: The user's input representing their chosen move.
    """
    if counter == 0 or counter % 2 == 0:
        return input(f"{PLAYER_O} enters a move: ")
    else:
        return input(f"{PLAYER_X} enters a move: ")


def main_game() -> None:
    """
    The main game loop for Tic-Tac-Toe.
    Handles turn progression, input, board updates, and win/draw checks.
    """
    GAME_RUNNING: bool = True
    counter: int = 0

    while GAME_RUNNING and counter < 9:
        move: str = whose_turn_it_is(counter)

        # Validate move input
        if move in board.keys():
            if board[move] is None:
                # Assign move based on the turn
                if counter % 2 == 0 or counter == 0:
                    board[move] = f"{PLAYER_O}"
                    counter += 1
                elif counter % 2 != 0 or counter == 1:
                    board[move] = f"{PLAYER_X}"
                    counter += 1
                elif counter == 8:
                    print("DRAW")
                    GAME_RUNNING = False
            else:
                print("Occupied")
        else:
            print("Invalid move")
            continue

        print_board(board)

        # Check if someone has won
        if is_there_a_winner(board, counter)[0] is False:
            GAME_RUNNING = False
            print(is_there_a_winner(board, counter)[1])


# Start the game
main_game()
