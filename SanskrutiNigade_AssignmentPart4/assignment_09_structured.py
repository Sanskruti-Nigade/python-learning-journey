"""
Assignment 9: Structured Arrays
"""
import numpy as np

def problem_1():
    print("--- Problem 1: Structured Array Sorting ---")
    # Define structured layout types
    dtype = [('name', 'U20'), ('age', 'i4'), ('weight', 'f4')]
    
    # Input records
    data = [('Alice', 25, 55.5), ('Bob', 30, 75.2), ('Charlie', 22, 68.0)]
    structured_arr = np.array(data, dtype=dtype)
    print("Original Structured Array:\n", structured_arr)

    # Sort the array by fields matching 'age'
    sorted_arr = np.sort(structured_arr, order='age')
    print("\nSorted Structured Array by Age:\n", sorted_arr)

def problem_2():
    print("\n--- Problem 2: Pairwise Euclidean Distance Matrix ---")
    # Define fields for coordinates
    dtype_coords = [('x', 'i4'), ('y', 'i4')]
    
    # Points pool
    points_data = [(1, 2), (4, 6), (7, 2)]
    points = np.array(points_data, dtype=dtype_coords)
    print("Points array:", points)

    # Extract x and y coordinates
    x = points['x']
    y = points['y']

    # Matrix operations via broadcasting to compute pairwise distances
    dist_matrix = np.sqrt((x[:, np.newaxis] - x)**2 + (y[:, np.newaxis] - y)**2)
    print("\nPairwise Euclidean Distance Matrix:\n", dist_matrix)

if __name__ == "__main__":
    problem_1()
    problem_2()