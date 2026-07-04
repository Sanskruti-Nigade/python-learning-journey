import pandas as pd

print("--- Assignment 10.1 ---")
s1 = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])
s1_upper = s1.str.upper()
print("Uppercase Series:\n", s1_upper)

print("\n--- Assignment 10.2 ---")
s2 = pd.Series(['Python', 'Pandas', 'Numpy', 'Matplotlib', 'Seaborn'])
s2_sliced = s2.str[:3]
print("First 3 characters:\n", s2_sliced)