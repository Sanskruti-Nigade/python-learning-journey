def maxArea(height: list[int]) -> int:
    """
    Finds the maximum amount of water a container can store.
    Time Complexity: O(n) - Single pass through the array.
    Space Complexity: O(1) - Constant memory utilized.
    """
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Width is the distance between the two vertical lines
        width = right - left
        
        # The water height is bounded by the shorter line
        current_height = min(height[left], height[right])
        
        # Calculate current water capacity
        current_water = width * current_height
        
        # Update max_water if the current container holds more
        max_water = max(max_water, current_water)
        
        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 4. Container With Most Water Test ---")
    
    # Test Case 1: Standard LeetCode example
    input_height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Max water for {input_height1}: {maxArea(input_height1)}") 
    # Expected Output: 49 (Lines at index 1 and index 8 form the optimal container)

    # Test Case 2: Minimal array size
    input_height2 = [1, 1]
    print(f"Max water for {input_height2}: {maxArea(input_height2)}") 
    # Expected Output: 1