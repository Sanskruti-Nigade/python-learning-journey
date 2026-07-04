def longestCommonPrefix(strs: list[str]) -> str:
    """
    Finds the longest common prefix among an array of strings.
    Time Complexity: O(N * M log N) where N is number of strings and M is max string length (due to sorting).
    Space Complexity: O(1) if sorting in place, or O(N) depending on Python's Timsort overhead.
    """
    if not strs:
        return "-1"
        
    # Sort the array alphabetically
    strs.sort()
    
    # Compare the first and the last string
    first = strs[0]
    last = strs[-1]
    
    i = 0
    # Match characters as long as they are equal and within bounds
    while i < min(len(first), len(last)) and first[i] == last[i]:
        i += 1
        
    # Extract the prefix
    prefix = first[:i]
    
    # If no common prefix exists, GFG expects "-1"
    return prefix if prefix != "" else "-1"


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 6. Longest Common Prefix Test ---")
    
    # Test Case 1: Standard common prefix
    arr1 = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(f"Strings: {arr1}")
    print(f"Longest Common Prefix: {longestCommonPrefix(arr1)}") 
    # Expected Output: "gee"

    # Test Case 2: No common prefix
    arr2 = ["hello", "world", "python"]
    print(f"\nStrings: {arr2}")
    print(f"Longest Common Prefix: {longestCommonPrefix(arr2)}") 
    # Expected Output: "-1"