from aocd import get_aoc_data
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# import data
start = get_aoc_data(2022, 6).reset_index()

# get individual chars into list
chars = start['data'].apply(lambda x: list(x)).tolist()[0]


def find_first_unique_packet(chars_lst, num):

    # define lst length
    lst_len = len(chars_lst)
    # set start and end point for chars
    i = 0
    j = i + num

    # initiate loop until answer found
    while j < lst_len:
        i += 1
        j += 1
        check = chars_lst[i:j]
        # check unique chars
        if len(set(check)) == num:
            return j


# part 1
print('pt1:', find_first_unique_packet(chars, 4))

# part 2
print('pt2:', find_first_unique_packet(chars, 14))
