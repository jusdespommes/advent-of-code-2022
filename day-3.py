from aocd import get_aoc_data
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# test data
# data = pd.read_csv(r'C:\Users\Alex.SJones\OneDrive - JLL\AJ Files\git\advent-of-code-2022\test-data\day-2.csv')

# import data
data = get_aoc_data(2022, 3)

data['pack_count'] = data['data'].apply(lambda x: len(x))

data['compartment_size'] = data['pack_count']/2

data['1'] = data.apply(lambda x: x['data'].str[0:x['compartment_size']])
print(data)