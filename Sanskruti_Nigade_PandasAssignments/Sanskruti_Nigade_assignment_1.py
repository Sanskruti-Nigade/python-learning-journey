import pandas as pd
import numpy as np

# Set seed for reproducible outputs
np.random.seed(42)

print("--- Assignment 1.1 ---")
# 1. 4 columns, 6 rows, set index to first column
df1_1 = pd.DataFrame(np.random.randint(0, 100, size=(6, 4)), columns=['Col1', 'Col2', 'Col3', 'Col4'])
df1_1.set_index('Col1', inplace=True)
print(df1_1)

print("\n--- Assignment 1.2 ---")
# 2. Specific columns and index, access element
df1_2 = pd.DataFrame(np.random.randint(0, 100, size=(3, 3)), columns=['A', 'B', 'C'], index=['X', 'Y', 'Z'])
element = df1_2.loc['Y', 'B']
print("DataFrame:\n", df1_2)
print(f"\nElement at row 'Y' and column 'B': {element}")