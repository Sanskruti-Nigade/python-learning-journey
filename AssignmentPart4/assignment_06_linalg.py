"""
Assignment 6: Linear Algebra
"""
import numpy as np

def problem_1():
    print("--- Problem 1: Determinant, Inverse, and Eigenvalues ---")
    # Create an invertible 3x3 matrix
    matrix = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 2]], dtype=float)
    print("Matrix:\n", matrix)

    det = np.linalg.det(matrix)
    inv = np.linalg.inv(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    print(f"\nDeterminant: {det:.4f}")
    print("\nInverse Matrix:\n", inv)
    print("\nEigenvalues:\n", eigenvalues)

def problem_2():
    print("\n--- Problem 2: Matrix Multiplication ---")
    # Create a (2, 3) and a (3, 2) array
    mat1 = np.random.randint(1, 5, size=(2, 3))
    mat2 = np.random.randint(1, 5, size=(3, 2))
    
    print("Matrix 1 (2x3):\n", mat1)
    print("Matrix 2 (3x2):\n", mat2)

    # Matrix multiplication (Dot product)
    product = mat1 @ mat2 # Alternatively: np.dot(mat1, mat2)
    print("\nResult Matrix (2x2):\n", product)

if __name__ == "__main__":
    problem_1()
    problem_2()