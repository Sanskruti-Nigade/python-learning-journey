def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# --- ADD THESE LINES TO RUN AND TEST IT ---

# Test Case 1: Should return True (2 is a duplicate)
test_array_1 = [1, 2, 3, 2]
result_1 = containsDuplicate(test_array_1)
print(f"Result for {test_array_1}: {result_1}")

# Test Case 2: Should return False (all distinct)
test_array_2 = [1, 2, 3, 4]
result_2 = containsDuplicate(test_array_2)
print(f"Result for {test_array_2}: {result_2}")