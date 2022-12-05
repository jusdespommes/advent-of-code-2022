from aocd import get_aoc_data
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# import data
original_data = get_aoc_data(2022, 4)

# split out cells
data = original_data['data'].str.split(',', n=1, expand=True)

# rename cols
data = data.rename(columns={0: '1', 1: '2'})

# split each assignment into minmax
data[['min1', 'max1']] = data['1'].str.split('-', n=1, expand=True)
data[['min2', 'max2']] = data['2'].str.split('-', n=1, expand=True)

# convert to int
data = data[['min1', 'max1', 'min2', 'max2']].astype(int)


def flag_row_contained_exactly(row):
    if ((row['min2'] >= row['min1']) & (row['max2'] <= row['max1'])) | ((row['min1'] >= row['min2']) & (row['max1'] <= row['max2'])):
        return 1


# find rows contained completely in one or other assignment
data['flag_pt1'] = data.apply(flag_row_contained_exactly, axis=1)

print(data['flag_pt1'].sum())


def flag_row_contained_approximately(row):
    if (row['min2'] <= row['max1']) & (row['min1'] <= row['max2']):
        return 1


# find rows part contained in one or other assignment
data['flag_pt2'] = data.apply(flag_row_contained_approximately, axis=1)

print(data['flag_pt2'].sum())
