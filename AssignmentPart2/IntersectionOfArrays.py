def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Finds unique common elements between two integer arrays using sets.
    Time Complexity: O(n + m) - To create sets and find the intersection.
    Space Complexity: O(n + m) - To store elements inside the sets.
    """
    # Convert both lists to sets and compute their intersection
    # The '&' operator extracts elements present in BOTH sets
    unique_intersection = set(nums1) & set(nums2)
    
    # Convert the resulting set back into a list
    return list(unique_intersection)


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 13. Intersection of Two Arrays Test ---")
    
    # Test Case 1: Simple intersection with duplicate elements
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    print(f"Array 1: {arr1}, Array 2: {arr2}")
    print(f"Intersection: {intersection(arr1, arr2)}") 
    # Expected Output: [2]

    # Test Case 2: Multi-element intersection
    arr3 = [4, 9, 5]
    arr4 = [9, 4, 9, 8, 4]
    print(f"\nArray 3: {arr3}, Array 4: {arr4}")
    print(f"Intersection: {intersection(arr3, arr4)}") 
    # Expected Output: [4, 9] (or [9, 4], order does not matter)