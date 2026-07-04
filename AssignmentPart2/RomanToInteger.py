def romanToInt(s: str) -> int:
    """
    Converts a Roman numeral string into an integer.
    Time Complexity: O(n) - Single pass through the string s.
    Space Complexity: O(1) - The map size is fixed.
    """
    # Dictionary containing standard Roman numeral conversions
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        # Check if the current value is less than the next value
        if i + 1 < n and roman_map[s[i]] < roman_map[s[i+1]]:
            # Subtract instead of add (e.g., IV where I < V)
            total -= roman_map[s[i]]
        else:
            # Standard addition
            total += roman_map[s[i]]
            
    return total


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 14. Roman to Integer Test ---")
    
    # Test Case 1: Simple additive Roman numeral
    str1 = "LVIII"
    print(f"Roman: {str1} -> Integer: {romanToInt(str1)}") 
    # Expected Output: 58 (L = 50, V = 5, III = 3)

    # Test Case 2: Roman numeral with subtraction rules
    str2 = "MCMXCIV"
    print(f"Roman: {str2} -> Integer: {romanToInt(str2)}") 
    # Expected Output: 1994 (M = 1000, CM = 900, XC = 90, IV = 4)