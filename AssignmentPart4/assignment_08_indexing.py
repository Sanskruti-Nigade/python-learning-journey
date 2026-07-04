"""
Assignment 8: Fancy Indexing and Boolean Indexing
"""
import numpy as np

def problem_1():
    print("--- Problem 1: Fancy Indexing (Corners) ---")
    # Create a 5x5 array with random integers
    arr = np.random.randint(10, 100, size=(5, 5))
    print("Original Array:\n", arr)

    # Zip target coordinate lists to target the corners
    row_idx = [0, 0, -1, -1]
    col_idx = [0, -1, 0, -1]
    
    corners = arr[row_idx, col_idx]
    print("\nExtracted Corners [Top-Left, Top-Right, Bottom-Left, Bottom-Right]:")
    print(corners)

def problem_2():
    print("\n--- Problem 2: Boolean Indexing (Clipping) ---")
    # Create a 4x4 array with random integers
    arr = np.random.randint(1, 20, size=(4, 4))
    print("Original Array:\n", arr)

    # Use boolean mapping to replace values > 10 with 10
    arr[arr > 10] = 10
    print("\nModified Array (Elements > 10 capped at 10):\n", arr)

if __name__ == "__main__":
    problem_1()
    problem_2()