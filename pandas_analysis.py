import numpy as np
import pandas as pd

# 1. Create a Series containing ten random numbers
# Generates 10 random numbers between 0 and 100
np.random.seed(42)  # Setting a seed for reproducible results
random_data = np.random.randint(0, 100, size=100)
series = pd.Series(random_data[:10])
print("--- Original Pandas Series ---")
print(series)
print("\n" + "=" * 40 + "\n")

# 2. Indexing Operations
print("--- Indexing Operations ---")
# Accessing a single element (e.g., the element at index 3)
single_element = series[3]
print(f"Element at index 3: {single_element}")

# Slicing the series (e.g., getting elements from index 2 up to 5)
sliced_series = series[2:6]
print("\nSliced Series (indices 2 to 5):")
print(sliced_series)
print("\n" + "=" * 40 + "\n")

# 3. Filtering Operations
print("--- Filtering Operations ---")
# Filter values greater than 50
filtered_series = series[series > 50]
print("Elements greater than 50:")
print(filtered_series)
print("\n" + "=" * 40 + "\n")

# 4. Statistical Operations
print("--- Statistical Operations ---")
series_mean = series.mean()
series_median = series.median()
series_min = series.min()
series_max = series.max()

print(f"Mean (Average): {series_mean}")
print(f"Median (Middle Value): {series_median}")
print(f"Minimum Value: {series_min}")
print(f"Maximum Value: {series_max}")
