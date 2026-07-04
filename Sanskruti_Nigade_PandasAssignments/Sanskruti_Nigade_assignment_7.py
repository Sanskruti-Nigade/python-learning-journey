import pandas as pd
import numpy as np

print("--- Assignment 7.1 ---")
# 1. MultiIndex Basic Slicing
arrays = [['East', 'East', 'West', 'West'], ['Q1', 'Q2', 'Q1', 'Q2']]
index = pd.MultiIndex.from_arrays(arrays, names=('Region', 'Quarter'))
df7_1 = pd.DataFrame(np.random.randint(100, 500, size=(4, 2)), index=index, columns=['Sales', 'Profit'])
print("MultiIndex DF:\n", df7_1)
print("\nSlice 'East' Region:\n", df7_1.loc['East'])

print("\n--- Assignment 7.2 ---")
# 2. Sum for Category and SubCategory
cat_sub = [['Electronics', 'Electronics', 'Furniture', 'Furniture'], ['TV', 'Laptop', 'Chair', 'Table']]
index7_2 = pd.MultiIndex.from_arrays(cat_sub, names=('Category', 'SubCategory'))
df7_2 = pd.DataFrame(np.random.randint(10, 100, size=(4, 1)), index=index7_2, columns=['Units'])
print("Sum by Category:\n", df7_2.groupby('Category').sum())
print("\nSum by SubCategory:\n", df7_2.groupby('SubCategory').sum())