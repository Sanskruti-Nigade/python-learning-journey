import pandas as pd
import numpy as np

print("--- Assignment 3.1 ---")
# 1. Fill NaNs with column mean
df3_1 = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)).astype(float), columns=['A', 'B', 'C'])
df3_1.iloc[0, 1] = np.nan
df3_1.iloc[2, 2] = np.nan
print("Original with NaNs:\n", df3_1)

df3_1_filled = df3_1.fillna(df3_1.mean())
print("\nFilled with Mean:\n", df3_1_filled)

print("\n--- Assignment 3.2 ---")
# 2. Drop rows with NaNs
df3_2 = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)).astype(float))
df3_2.iloc[1, 2] = np.nan
df3_2.iloc[4, 0] = np.nan
print("Original with NaNs:\n", df3_2)

df3_2_dropped = df3_2.dropna()
print("\nRows dropped:\n", df3_2_dropped)