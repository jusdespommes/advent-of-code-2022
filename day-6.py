import re
from aocd import get_aoc_data
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# import data
start = get_aoc_data(2022, 6).reset_index()

start['item'] = start['data'].apply(lambda x: re.findall('.', x))

start = start.explode(['item'])

chars = list(start['item'])


def find_first_unique_packet(chars_lst, num):

    lst_len = len(chars_lst)
    i = 0
    j = i + num

    while j < lst_len:
        i += 1
        j += 1
        check = chars_lst[i:j]
        if len(set(check)) == num:
            return j


# part 1
print('pt1:', find_first_unique_packet(chars, 4))

# part 2
print('pt2:', find_first_unique_packet(chars, 14))
