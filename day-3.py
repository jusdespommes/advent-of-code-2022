from aocd import get_aoc_data
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# test data
# data = pd.read_csv(r'C:\Users\Alex.SJones\OneDrive - JLL\AJ Files\git\advent-of-code-2022\test-data\day-2.csv')

# import data
original_data = get_aoc_data(2022, 3)

data = original_data.copy(deep=True)

# spec lookup
lookup = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

# get length of data
data['pack_count'] = data['data'].apply(lambda x: len(x))

# half for split
data['compartment_size'] = (data['pack_count']/2).astype(int)


def split_left(row):
    return row['data'][0:row['compartment_size']]


def split_right(row):
    return row['data'][row['compartment_size']:]


# create compartments
data['1'] = data.apply(split_left, axis=1)
data['2'] = data.apply(split_right, axis=1)

# remove other fields
data = data[['1', '2']]

# create list from 1st field
data['1a'] = data['1'].apply(lambda x: list(x))


def check_chars_appear(row):
    cmn_chars = set()
    for char in row['1a']:
        if char in row['2']:
            cmn_chars.add(char)
    return ', '.join(cmn_chars)


# find character that appears in 1 and 2
data['3'] = data.apply(check_chars_appear, axis=1)

data = data[['1', '2', '3']]

# map lookup list to get value
data['4'] = data['3'].map(lookup).astype(int)

# sum to get part 1 answer
print(data['4'].sum())

p2_data = original_data.copy(deep=True)

# group every 3 instances
p2_data['group'] = np.divmod(np.arange(len(p2_data)), 3)[0] + 1

# row id per group
p2_data['row_id'] = p2_data.groupby(['group']).cumcount()+1

# pivot data
p2_data = p2_data.pivot(index='group', columns='row_id', values='data').reset_index()

# create list from 1st/2nd field
p2_data['1a'] = p2_data[1].apply(lambda x: list(x))
p2_data['2a'] = p2_data[2].apply(lambda x: list(x))


def check_chars_appear_in_three(row):
    cmn_chars = set()
    first_group = []
    for char in row['1a']:
        if char in row[2]:
            first_group.append(char)
    for char in first_group:
        if char in row[3]:
            cmn_chars.add(char)
    return ', '.join(cmn_chars)


# find character that appears in 1 and 2
p2_data['4'] = p2_data.apply(check_chars_appear_in_three, axis=1)

# filter non-common entries
p2_data = p2_data[p2_data['4'] != '']

# map lookup list to get value
p2_data['5'] = p2_data['4'].map(lookup).astype(int)

print(p2_data['5'].sum())




