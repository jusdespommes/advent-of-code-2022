from aocd import get_aoc_data
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# import data
data = get_aoc_data(2022, 1)

# each blank row we attribute a 1
data['new_row'] = data['data'].apply(lambda x: 1 if (x == '') else 0)

# cumulative sum the new row flag
data['person_num'] = data['new_row'].cumsum()

# convert series column to number
data['calories'] = pd.to_numeric(data['data'], errors='coerce')

# group by and sum
calories_per_person = data.groupby(by=['person_num'])[['calories']].sum()

# sort values
# part 1 // calories of max 1 person
most_calories = calories_per_person.sort_values(by=['calories'], ascending=False).head(1)

# part 2 // total calories of 3 max people
top_3_calories = calories_per_person.sort_values(by=['calories'], ascending=False).head(3).sum()
print(top_3_calories)
