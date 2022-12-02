from aocd import get_aoc_data
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# test data
# data = pd.read_csv(r'C:\Users\Alex.SJones\OneDrive - JLL\AJ Files\git\advent-of-code-2022\test-data\day-2.csv')

# import data
data = get_aoc_data(2022, 2)

# split column to p1 and p2
prs = data["data"].str.split(" ", n=1, expand=True)

# reassign column names
prs.columns = ['p1', 'p2']

# filter out blank end row
prs = prs[prs['p2'].notnull()]

# replace paper, rocks, scissors with numerical vals
num_prs = prs.replace({'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3})

# replace paper, rocks, scissors with num and other vals for pt2
num_prs_pt2 = prs.replace({'A': 1, 'B': 2, 'C': 3, 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'})

# convert cols to int
num_prs[['p1', 'p2']] = num_prs[['p1', 'p2']].apply(pd.to_numeric)
num_prs_pt2['p1'] = num_prs_pt2['p1'].apply(pd.to_numeric)


# work out result of each round pt1
def round_result_pt1(p1score, p2score):
    if p1score == p2score:
        return p2score + 3
    elif (p2score == 3) & (p1score == 1):
        return p2score
    elif (p2score == 1) & (p1score == 3):
        return p2score + 6
    elif p2score > p1score:
        return p2score + 6
    else:
        return p2score


num_prs['round_score'] = num_prs.apply(lambda x: round_result_pt1(x['p1'], x['p2']), axis=1)

part_1_score = num_prs['round_score'].sum()


# work out result of each round
def round_result_pt2(p1score, p2result):
    if p2result == 'Draw':
        return p1score
    elif (p2score == 3) & (p1score == 1):
        return p2score
    elif (p2score == 1) & (p1score == 3):
        return p2score + 6
    elif p2score > p1score:
        return p2score + 6
    else:
        return p2score


print(num_prs_pt2)
