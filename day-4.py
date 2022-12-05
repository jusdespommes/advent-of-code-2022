from aocd import get_aoc_data
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# import data
original_data = get_aoc_data(2022, 4)

data = original_data["data"].str.split(",", n=1, expand=True)

print(data.head())
data = data.pivot(index=data.index, values=['0', '1'])
print(data)