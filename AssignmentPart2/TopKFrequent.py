from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Finds the k most frequent elements in an array.
    Time Complexity: O(N log K) where N is the number of elements.
    Space Complexity: O(N) to store elements in the frequency map.
    """
    # Step 1: Count the frequency of each element
    # e.g., [1,1,1,2,2,3] -> {1: 3, 2: 2, 3: 1}
    count_map = Counter(nums)
    
    # Step 2: Extract the k most common elements
    # most_common(k) returns a list of tuples: [(element, frequency), ...]
    # e.g., for k=2 -> [(1, 3), (2, 2)]
    frequent_tuples = count_map.most_common(k)
    
    # Step 3: Use list comprehension to extract just the elements (the first item in each tuple)
    return [item[0] for item in frequent_tuples]


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 11. Top K Frequent Elements Test ---")
    
    # Test Case 1: Standard match
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Array: {nums1}, K: {k1}")
    print(f"Top {k1} elements: {topKFrequent(nums1, k1)}") 
    # Expected Output: [1, 2]

    # Test Case 2: Array with single element
    nums2 = [1]
    k2 = 1
    print(f"\nArray: {nums2}, K: {k2}")
    print(f"Top {k2} elements: {topKFrequent(nums2, k2)}") 
    # Expected Output: [1]