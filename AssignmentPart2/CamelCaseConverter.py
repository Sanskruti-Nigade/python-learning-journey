def convertToCamelCase(s: str) -> str:
    """
    Converts a space-separated sentence into CamelCase format.
    Time Complexity: O(n) - Single pass to split and process characters.
    Space Complexity: O(n) - To hold the split words and final string.
    """
    # Split the sentence into individual words (handles multiple spaces automatically)
    words = s.split()
    
    if not words:
        return ""
        
    # Lowercase the first word, capitalize the rest, and join them
    first_word = words[0].lower()
    other_words = "".join(word.capitalize() for word in words[1:])
    
    return first_word + other_words


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 7. Convert Sentence to CamelCase Test ---")
    
    # Test Case 1: Standard sentence
    sentence1 = "I love python programming"
    print(f"Original: '{sentence1}'")
    print(f"CamelCase: '{convertToCamelCase(sentence1)}'") 
    # Expected Output: "iLovePythonProgramming"

    # Test Case 2: Sentence with random casing and extra spaces
    sentence2 = "  hello   WORLD   how ARE yOu "
    print(f"\nOriginal: '{sentence2}'")
    print(f"CamelCase: '{convertToCamelCase(sentence2)}'") 
    # Expected Output: "helloWorldHowAreYou"