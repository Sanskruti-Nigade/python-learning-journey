import pandas as pd
import numpy as np

print("--- Assignment 5.1 ---")
# 1. Merge on common column
df5_1a = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df5_1b = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [50000, 60000, 70000]})
merged_df = pd.merge(df5_1a, df5_1b, on='ID', how='inner')
print("Merged DataFrame:\n", merged_df)

print("\n--- Assignment 5.2 ---")
# 2. Concatenate along rows and columns
df5_2a = pd.DataFrame(np.random.randint(1, 10, size=(3, 2)), columns=['A', 'B'])
df5_2b = pd.DataFrame(np.random.randint(10, 20, size=(3, 2)), columns=['C', 'D'])

concat_rows = pd.concat([df5_2a, df5_2b], axis=0, ignore_index=True)
concat_cols = pd.concat([df5_2a, df5_2b], axis=1)
print("Concat along rows (axis=0):\n", concat_rows)
print("\nConcat along columns (axis=1):\n", concat_cols)