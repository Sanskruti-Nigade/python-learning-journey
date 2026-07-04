"""
Assignment 5: Broadcasting
"""
import numpy as np

def problem_1():
    print("--- Problem 1: Broadcasting to Rows ---")
    # Create a 3x3 array and a 1D array of shape (3,)
    matrix = np.random.randint(1, 10, size=(3, 3))
    row_vec = np.array([1, 2, 3])
    
    print("Matrix:\n", matrix)
    print("Row Vector to add:", row_vec)

    # Row vector broadcasts cleanly to trailing dimensions automatically
    result = matrix + row_vec
    print("\nResult Matrix:\n", result)

def problem_2():
    print("\n--- Problem 2: Broadcasting to Columns ---")
    # Create a 4x4 array and a 1D array of shape (4,)
    matrix = np.random.randint(1, 10, size=(4, 4))
    col_vec = np.array([1, 2, 3, 4])
    
    print("Matrix:\n", matrix)
    print("Column Vector to subtract:", col_vec)

    # Reshape col_vec to (4, 1) so it properly broadcasts along the columns axis
    result = matrix - col_vec[:, np.newaxis]
    print("\nResult Matrix:\n", result)

if __name__ == "__main__":
    problem_1()
    problem_2()