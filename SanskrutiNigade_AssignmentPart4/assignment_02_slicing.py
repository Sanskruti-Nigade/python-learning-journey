"""
Assignment 2: Array Indexing and Slicing
"""
import numpy as np

def problem_1():
    print("--- Problem 1: Extract Sub-array ---")
    # Create a 6x6 array with values from 1 to 36
    arr = np.arange(1, 37).reshape(6, 6)
    print("Original Array:\n", arr)

    # Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns
    # Note: Rows 3 to 5 -> indices 2 to 4. Columns 2 to 4 -> indices 1 to 3.
    sub_arr = arr[2:5, 1:4]
    print("\nExtracted Sub-array (Rows 3-5, Cols 2-4):\n", sub_arr)

def problem_2():
    print("\n--- Problem 2: Extract Border Elements ---")
    # Create a 5x5 array with random integers
    arr = np.random.randint(1, 10, size=(5, 5))
    print("Original Array:\n", arr)

    # Extract the border elements
    top_row = arr[0, :]
    bottom_row = arr[-1, :]
    left_col = arr[1:-1, 0]    # Sliced to avoid duplicating corner elements
    right_col = arr[1:-1, -1]  # Sliced to avoid duplicating corner elements

    print("\nBorder Elements:")
    print("Top Row:   ", top_row)
    print("Bottom Row:", bottom_row)
    print("Left Col:  ", left_col)
    print("Right Col: ", right_col)

if __name__ == "__main__":
    problem_1()
    problem_2()