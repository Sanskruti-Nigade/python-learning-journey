"""
Assignment 1: Array Creation and Manipulation
"""
import numpy as np

def problem_1():
    print("--- Problem 1: 5x5 Random Array & Column Replacement ---")
    # Create a 5x5 array with random integers between 1 and 20
    arr = np.random.randint(1, 21, size=(5, 5))
    print("Original Array:\n", arr)

    # Replace all elements in the third column (index 2) with 1
    arr[:, 2] = 1
    print("\nModified Array (Third Column Replaced with 1):\n", arr)

def problem_2():
    print("\n--- Problem 2: 4x4 Array & Diagonal Replacement ---")
    # Create a 4x4 array with values from 1 to 16
    arr = np.arange(1, 17).reshape(4, 4)
    print("Original Array:\n", arr)

    # Replace the diagonal elements with 0
    np.fill_diagonal(arr, 0)
    print("\nModified Array (Diagonal Replaced with 0):\n", arr)

if __name__ == "__main__":
    problem_1()
    problem_2()