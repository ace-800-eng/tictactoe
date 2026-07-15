#!/usr/bin/env python3
"""A simple Tic-Tac-Toe game played in the terminal."""

from __future__ import annotations

import random
from typing import List, Optional, Tuple

BOARD_SIZE = 3
WINNING_LINES = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


def print_board(board: List[List[str]]) -> None:
    print()
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if row != board[-1]:
            print("---+---+---")
    print()


def available_moves(board: List[List[str]]) -> List[Tuple[int, int]]:
    return [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == " "]


def has_won(board: List[List[str]], player: str) -> bool:
    for line in WINNING_LINES:
        if all(board[r][c] == player for r, c in line):
            return True
    return False


def is_draw(board: List[List[str]]) -> bool:
    return not available_moves(board)


def human_move(board: List[List[str]]) -> Tuple[int, int]:
    while True:
        choice = input("Choose a position from 1 to 9: ").strip()
        if not choice.isdigit():
            print("Please enter a number.")
            continue

        index = int(choice) - 1
        row, col = divmod(index, BOARD_SIZE)
        if 0 <= index <= 8 and board[row][col] == " ":
            return row, col

        print("That square is already taken or out of range. Try again.")


def computer_move(board: List[List[str]]) -> Tuple[int, int]:
    for move in available_moves(board):
        board_copy = [row[:] for row in board]
        r, c = move
        board_copy[r][c] = "O"
        if has_won(board_copy, "O"):
            return move

    for move in available_moves(board):
        board_copy = [row[:] for row in board]
        r, c = move
        board_copy[r][c] = "X"
        if has_won(board_copy, "X"):
            return move

    if (1, 1) in available_moves(board):
        return (1, 1)

    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [move for move in corners if move in available_moves(board)]
    if available_corners:
        return random.choice(available_corners)

    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    available_edges = [move for move in edges if move in available_moves(board)]
    if available_edges:
        return random.choice(available_edges)

    return random.choice(available_moves(board))


def play_game() -> None:
    board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The computer is O.")
    print("Choose a position from 1 to 9:")
    print("1 | 2 | 3")
    print("---+---+---")
    print("4 | 5 | 6")
    print("---+---+---")
    print("7 | 8 | 9")

    while True:
        print_board(board)

        if current_player == "X":
            row, col = human_move(board)
            board[row][col] = "X"
        else:
            print("Computer is thinking...")
            row, col = computer_move(board)
            board[row][col] = "O"

        if has_won(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted.")
