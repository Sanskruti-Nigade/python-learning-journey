def fizzBuzz(n: int) -> list[str]:
    """
    Iterates from 1 to n and returns a list based on divisibility rules.
    Time Complexity: O(n)
    Space Complexity: O(1) (excluding the output list)
    """
    res = []
    for i in range(1, n + 1):
        # Always check the combined condition first
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 3. Fizz Buzz Test ---")
    
    # Test Case 1: Small n to see basic replacements
    print("Output for n=5:", fizzBuzz(5)) 
    # Expected: ['1', '2', 'Fizz', '4', 'Buzz']

    # Test Case 2: Up to 15 to check the "FizzBuzz" condition
    print("\nOutput for n=15:")
    print(fizzBuzz(15))
    # Expected ends with '13', '14', 'FizzBuzz'