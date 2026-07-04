import pandas as pd
import numpy as np

print("--- Assignment 9.1 ---")
# 1. Double values across DataFrame
df9_1 = pd.DataFrame(np.random.randint(1, 10, size=(5, 3)))
print("Original:\n", df9_1)
df9_1_doubled = df9_1.apply(lambda x: x * 2)
print("\nDoubled:\n", df9_1_doubled)

print("\n--- Assignment 9.2 ---")
# 2. Lambda for row-wise sum to new column
df9_2 = pd.DataFrame(np.random.randint(1, 10, size=(6, 3)), columns=['A', 'B', 'C'])
df9_2['Total'] = df9_2.apply(lambda row: row['A'] + row['B'] + row['C'], axis=1)
print(df9_2)