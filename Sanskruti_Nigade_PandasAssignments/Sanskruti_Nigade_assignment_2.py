import pandas as pd
import numpy as np

print("--- Assignment 2.1 ---")
# 1. Product of first two columns
df2_1 = pd.DataFrame(np.random.randint(1, 10, size=(5, 3)), columns=['Col1', 'Col2', 'Col3'])
df2_1['Product'] = df2_1['Col1'] * df2_1['Col2']
print(df2_1)

print("\n--- Assignment 2.2 ---")
# 2. Row-wise and column-wise sum
df2_2 = pd.DataFrame(np.random.randint(1, 10, size=(4, 3)))
print("DataFrame:\n", df2_2)
print("\nRow-wise sum:\n", df2_2.sum(axis=1))
print("\nColumn-wise sum:\n", df2_2.sum(axis=0))