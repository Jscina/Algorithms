# Future import not necessary if python >= 3.10
from __future__ import annotations
import random

op_count = 0


def MatrixMultiplication(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Multiplies two matrices A and B and counts the basic operations being performed."""
    global op_count
    # Init the result matrix with same dimensions as A and B, filled with 0s
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = 0  # First basic operation, redundant, but it's in the pseudocode
            op_count += 1
            for k in range(len(A)):
                op_count += 3
                C[i][j] += A[i][k] * B[k][j]  # Second basic operation
    return C


def generate_random_matrix(n: int) -> list[list[int]]:
    """Generates a random matrix of size n x n"""
    return [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]


def main():
    global op_count
    for i in [1, 10, 100]:
        op_count = 0  # Reset the operation count
        m1, m2 = generate_random_matrix(i), generate_random_matrix(i)
        print(f"{i} X {i} : \n", MatrixMultiplication(m1, m2), sep=" ", end="\n\n")
        print(op_count, "operations performed")


if __name__ == "__main__":
    main()
