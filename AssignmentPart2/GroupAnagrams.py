from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Groups anagrams together using a hash map with sorted string keys.
    Time Complexity: O(n * m log m) where n is number of strings, m is max string length.
    Space Complexity: O(n * m) to store the hash map data.
    """
    # Use a dictionary that automatically creates an empty list if a key doesn't exist yet
    anagrams = defaultdict(list)
    
    for s in strs:
        # Sort the characters of the string to create a unique key
        # e.g., "tea" -> ['a', 'e', 't'] -> "aet"
        sorted_key = "".join(sorted(s))
        
        # Append the original string to the matching anagram list
        anagrams[sorted_key].append(s)
        
    # Return just the grouped lists of words
    return list(anagrams.values())


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 9. Group Anagrams Test ---")
    
    # Test Case 1: Standard mix of anagrams
    words1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Original list: {words1}")
    print("Grouped Anagrams:")
    print(groupAnagrams(words1))
    # Expected Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (order may vary)

    # Test Case 2: Array with single or empty strings
    words2 = ["", "b"]
    print(f"\nOriginal list: {words2}")
    print("Grouped Anagrams:")
    print(groupAnagrams(words2))
    # Expected Output: [[''], ['b']]