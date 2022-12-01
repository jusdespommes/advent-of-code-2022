import requests
import pandas as pd


def get_aoc_data(year: str, day_number: str):

    cookie = r'_ga=GA1.2.1577261669.1669890232; _gid=GA1.2.1007606226.1669890232; session=53616c7465645f5fedc12e6783a57ecb88f4e14e7337912f8358ec995eca1c3595de6ce48c9256c94a5485df304de37d1a8eb680c93bc09e3fc913ae7bfa7ec8; _gat=1'

    url = f'https://adventofcode.com/{year}/day/{day_number}/input'
    headers = {'user-agent': 'Mozilla/5.0', 'cookie': cookie}

    get_data = requests.get(url, headers=headers)
    data_returned = get_data.text.split('\n')
    data_dataframe = pd.DataFrame(columns=['data'], data=data_returned)

    return data_dataframe

