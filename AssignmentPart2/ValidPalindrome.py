def isPalindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    Time Complexity: O(n) - Single pass to clean the string and another to check reversal.
    Space Complexity: O(n) - To store the cleaned version of the string.
    """
    # Filter out non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 5. Valid Palindrome Test ---")
    
    # Test Case 1: Standard palindrome sentence with punctuation and spaces
    str1 = "A man, a plan, a canal: Panama"
    print(f"Is '{str1}' a palindrome?: {isPalindrome(str1)}") 
    # Expected Output: True ("amanaplanacanalpanama")

    # Test Case 2: Non-palindrome string
    str2 = "race a car"
    print(f"Is '{str2}' a palindrome?: {isPalindrome(str2)}") 
    # Expected Output: False ("raceacar" != "racaecar")
    
    # Test Case 3: Empty or space-only string (considered valid by LeetCode)
    str3 = "   "
    print(f"Is '{str3}' a palindrome?: {isPalindrome(str3)}") 
    # Expected Output: True (empty string equals empty string)