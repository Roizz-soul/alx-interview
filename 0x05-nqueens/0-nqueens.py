#!/usr/bin/python3
"""
N queens
"""

import sys


def print_solutions(solutions):
    """Prints each solution in the specified format"""
    for solution in solutions:
        print(solution)


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """Utilize backtracking to solve the problem"""
    if col == N:
        # All queens are placed, add the solution
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack


def solve_nqueens(N):
    """Solves the N-Queens puzzle"""
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    print_solutions(solutions)


def main():
    """Main function to parse arguments and start the solver"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
