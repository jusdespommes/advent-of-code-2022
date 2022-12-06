import re
from aocd import get_aoc_data
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# import data
original_data = get_aoc_data(2022, 5).reset_index()

# create sub datasets
stacks = original_data[:8].copy(deep=True).sort_index(ascending=False).reset_index(drop=True)
commands = original_data[10:].copy(deep=True)

# add space to end of stacks
stacks['data'] = stacks['data'] + ' '

# split to each 4 chars in stacks
stacks['item'] = stacks['data'].apply(lambda x: re.findall('.{4}', x))


def clean_up_chars(row):
    clean_items = []
    for item in row['item']:
        item = item.replace('[', '').replace(']', '').replace(' ', '')
        clean_items.append(item)
    return clean_items


# remove unneeded chars
stacks['item'] = stacks.apply(clean_up_chars, axis=1)

print(stacks.head(10))

# tokenize to rows
stacks = stacks.explode(['item'])

# add id
stacks = stacks[['index', 'item']].reset_index()

# rename cols
stacks = stacks.rename(columns={'level_0': 'pos', 'index': 'id'})

# add stack id
stacks['stack'] = stacks.groupby(['pos']).cumcount() + 1

# add space at end of line to help with Regex parsing
stacks = stacks[stacks['item'] != ' ']

# replace blanks with nulls
stacks = stacks.replace(r'^\s*$', np.nan, regex=True)

# filter nulls
stacks = stacks[stacks['item'].notnull()].reset_index(drop=True)

# select cols
stacks = stacks[['pos', 'stack', 'item']]

# convert cols to ints
stacks[['pos', 'stack']] = stacks[['pos', 'stack']].astype(int)

# split out number commands
commands = commands['data'].str.split(r'(\d+)', n=3, expand=True)

# select cols
commands = commands[[1, 3, 5]]

# rename cols
commands = commands.rename(columns={1: 'num', 3: 'from', 5: 'to'}).reset_index(drop=True)

# add a record id
commands['order'] = commands.index

# convert all to int
commands = commands.astype(int)

commands = commands.head(1)


def order_command(cmd_row, sort_option):

    if cmd_row['order'] == 0:
        orig_stack = stacks[stacks['stack'] == cmd_row['from']]
        new_stack = stacks[stacks['stack'] == cmd_row['to']]
        other_stacks = stacks[(stacks['stack'] != cmd_row['from']) & (stacks['stack'] != cmd_row['to'])]

    max_pos = max(orig_stack['pos'])

    move_boxes = orig_stack[orig_stack['pos'] > (max_pos - cmd_row['num'])].sort_values(by=['pos'], ascending=sort_option)
    move_boxes = move_boxes[['stack', 'item']]
    move_boxes['stack'] = cmd_row['to']

    other_boxes = orig_stack[orig_stack['pos'] <= (max_pos - cmd_row['num'])]

    new_stack = pd.concat([new_stack, move_boxes]).reset_index(drop=True)
    new_stack['pos'] = new_stack.index

    stacks_copy = pd.concat([other_stacks, other_boxes, new_stack]).sort_values(by=['stack', 'pos']).reset_index(drop=True)
    # print(stacks_copy)


commands.apply(order_command, sort_option=False, axis=1)

