"""
Assignment 10: Masked Arrays
"""
import numpy as np
import numpy.ma as ma

def problem_1():
    print("--- Problem 1: Mask Values > 10 ---")
    # Create a 4x4 array with random integers
    arr = np.random.randint(1, 20, size=(4, 4))
    print("Original Array:\n", arr)

    # Mask conditional entries
    masked_arr = ma.masked_greater(arr, 10)
    print("\nMasked Array:\n", masked_arr)

    # Sum treats masked fields as empty/ignored
    print("\nSum of Unmasked Elements:", masked_arr.sum())

def problem_2():
    print("\n--- Problem 2: Mask & Impute Diagonal Entries ---")
    # Create a 3x3 float array
    arr = np.random.randint(1, 20, size=(3, 3)).astype(float)
    print("Original Array:\n", arr)

    # Structural boolean mapping matrix for identity mapping (diagonal layout)
    diag_mask = np.eye(3, dtype=bool)

    # Initialize masked instance
    masked_arr = ma.array(arr, mask=diag_mask)
    print("\nMasked Array (Diagonal Hidden):\n", masked_arr)

    # Gather clean stats and fill target mask layers
    unmasked_mean = masked_arr.mean()
    filled_arr = masked_arr.filled(unmasked_mean)
    
    print(f"\nMean of Unmasked Elements: {unmasked_mean:.4f}")
    print("Final Array (Diagonal filled with mean):\n", filled_arr)

if __name__ == "__main__":
    problem_1()
    problem_2()