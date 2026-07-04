"""
Assignment 3: Array Operations
"""
import numpy as np

def problem_1():
    print("--- Problem 1: Element-wise Operations ---")
    # Create two 3x4 arrays with random integers
    a = np.random.randint(1, 10, size=(3, 4))
    b = np.random.randint(1, 10, size=(3, 4))
    
    print("Array A:\n", a)
    print("Array B:\n", b)
    
    print("\nElement-wise Addition:\n", a + b)
    print("Element-wise Subtraction:\n", a - b)
    print("Element-wise Multiplication:\n", a * b)
    print("Element-wise Division:\n", a / b)

def problem_2():
    print("\n--- Problem 2: Row-wise and Column-wise Sum ---")
    # Create a 4x4 array with values from 1 to 16
    arr = np.arange(1, 17).reshape(4, 4)
    print("Original Array:\n", arr)

    row_sum = arr.sum(axis=1)
    col_sum = arr.sum(axis=0)

    print("\nRow-wise Sum:   ", row_sum)
    print("Column-wise Sum:", col_sum)

if __name__ == "__main__":
    problem_1()
    problem_2()