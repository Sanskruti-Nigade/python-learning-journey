def uniquePrimeFactors(n: int) -> list[int]:
    """
    Finds the unique prime factors of a given number n in increasing order.
    Time Complexity: O(sqrt(n))
    Space Complexity: O(number of unique prime factors)
    """
    factors = []
    
    # Check for factor 2
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2
            
    # Check for odd factors from 3 up to sqrt(n)
    d = 3
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 2  # Increment by 2 to check only odd numbers
        
    # If n is still greater than 1, then the remaining n is prime
    if n > 1:
        factors.append(n)
        
    return factors


# --- RUN AND TEST CASES ---
if __name__ == "__main__":
    print("--- 2. Unique Prime Factors ---")
    
    # Test Case 1: Standard composite number
    n1 = 35
    print(f"Unique prime factors of {n1}: {uniquePrimeFactors(n1)}") # Expected: [5, 7]

    # Test Case 2: Number with repeated prime factors (2 * 2 * 2 * 3 = 24)
    n2 = 24
    print(f"Unique prime factors of {n2}: {uniquePrimeFactors(n2)}") # Expected: [2, 3]

    # Test Case 3: A large prime number
    n3 = 97
    print(f"Unique prime factors of {n3}: {uniquePrimeFactors(n3)}") # Expected: [97]