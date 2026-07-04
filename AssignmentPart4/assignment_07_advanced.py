"""
Assignment 7: Advanced Array Manipulation
"""
import numpy as np

def problem_1():
    print("--- Problem 1: Sequential Reshaping ---")
    # Create a 3x3 array with values from 1 to 9
    arr = np.arange(1, 10).reshape(3, 3)
    print("Original 3x3 Array:\n", arr)

    # Reshape to (1, 9)
    row_vec = arr.reshape(1, 9)
    print("\nReshaped to (1, 9):\n", row_vec)

    # Reshape to (9, 1)
    col_vec = row_vec.reshape(9, 1)
    print("\nReshaped to (9, 1):\n", col_vec)

def problem_2():
    print("\n--- Problem 2: Flattening and Rebuilding ---")
    # Create a 5x5 array with random integers
    arr = np.random.randint(1, 50, size=(5, 5))
    print("Original 5x5 Array:\n", arr)

    # Flatten the array
    flat = arr.flatten()
    print("\nFlattened Array (1D):\n", flat)

    # Reshape it back to (5, 5)
    restored = flat.reshape(5, 5)
    print("\nRestored back to (5, 5):\n", restored)

if __name__ == "__main__":
    problem_1()
    problem_2()