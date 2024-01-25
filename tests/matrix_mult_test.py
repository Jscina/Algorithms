from algorithms.main import MatrixMultiplication, generate_random_matrix
import numpy as np


def test_matrix_multiplication_1_by_1():
    m1, m2 = generate_random_matrix(1), generate_random_matrix(1)
    expected = np.matmul(m1, m2).tolist()
    actual = MatrixMultiplication(m1, m2)
    assert actual == expected


def test_matrix_multiplication_10_by_10():
    m1, m2 = generate_random_matrix(10), generate_random_matrix(10)
    expected = np.matmul(m1, m2).tolist()
    actual = MatrixMultiplication(m1, m2)
    assert actual == expected


def test_matrix_multiplication_100_by_100():
    m1, m2 = generate_random_matrix(100), generate_random_matrix(100)
    expected = np.matmul(m1, m2).tolist()
    actual = MatrixMultiplication(m1, m2)
    assert actual == expected
