def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Finds indices of two numbers that add up to the target using a hash map.
    Time Complexity: O(n) - We loop through the array only once.
    Space Complexity: O(n) - In the worst case, we store all elements in the map.
    """
    # Hash map to store value to its index mapping
    prev_map = {}  # format -> { value: index }
    
    for i, n in enumerate(nums):
        diff = target - n
        
        # If the complement is already in the map, we found the solution
        if diff in prev_map:
            return [prev_map[diff], i]
            
        # Otherwise, store the current number and its index
        prev_map[n] = i
        
    return []  # Return empty list if no solution is found


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 10. Two Sum Test ---")
    
    # Test Case 1: Standard match
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Array: {nums1}, Target: {target1}")
    print(f"Indices: {twoSum(nums1, target1)}") 
    # Expected Output: [0, 1] (because nums[0] + nums[1] == 9)

    # Test Case 2: Elements are not sorted, target requires later elements
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\nArray: {nums2}, Target: {target2}")
    print(f"Indices: {twoSum(nums2, target2)}") 
    # Expected Output: [1, 2]