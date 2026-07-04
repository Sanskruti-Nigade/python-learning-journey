"""
Assignment 4: Statistical Operations
"""
import numpy as np

def problem_1():
    print("--- Problem 1: Basic Statistical Metrics ---")
    # Create a 5x5 array with random integers
    arr = np.random.randint(1, 100, size=(5, 5))
    print("Array:\n", arr)

    print("\nCalculated Stats:")
    print("Mean:              ", np.mean(arr))
    print("Median:            ", np.median(arr))
    print("Standard Deviation:", np.std(arr))
    print("Variance:          ", np.var(arr))

def problem_2():
    print("\n--- Problem 2: Array Normalization ---")
    # Create a 3x3 array with values from 1 to 9
    arr = np.arange(1, 10).reshape(3, 3).astype(float)
    print("Original Array:\n", arr)

    # Standardize (Mean = 0, Std = 1)
    mean = np.mean(arr)
    std = np.std(arr)
    normalized_arr = (arr - mean) / std
    
    print("\nNormalized Array:\n", normalized_arr)
    print(f"Verified Mean: {np.round(np.mean(normalized_arr))}, Verified Std: {np.std(normalized_arr)}")

if __name__ == "__main__":
    problem_1()
    problem_2()