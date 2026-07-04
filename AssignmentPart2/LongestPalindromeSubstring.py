def longestPalindrome(s: str) -> str:
    """
    Finds the longest palindromic substring in S using the Expand Around Center method.
    Time Complexity: O(n^2)
    Space Complexity: O(1) - Updates the result string in place.
    """
    res = ""
    
    for i in range(len(s)):
        # Case 1: Odd length palindromes (e.g., "aba", center is 'b')
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
            
        # Case 2: Even length palindromes (e.g., "abba", center is between 'b' and 'b')
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
            
    return res


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 8. Longest Palindromic Substring Test ---")
    
    # Test Case 1: Odd-length optimal palindrome
    str1 = "babad"
    print(f"String: '{str1}'")
    print(f"Longest Palindromic Substring: '{longestPalindrome(str1)}'") 
    # Expected Output: "bab" (or "aba" is also correct)

    # Test Case 2: Even-length absolute palindrome
    str2 = "cbbd"
    print(f"\nString: '{str2}'")
    print(f"Longest Palindromic Substring: '{longestPalindrome(str2)}'") 
    # Expected Output: "bb"