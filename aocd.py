import requests
import pandas as pd


def get_aoc_data(year: str, day_number: str):

    cookie = r'_ga=GA1.2.1577261669.1669890232; _gid=GA1.2.1007606226.1669890232; session=53616c7465645f5f7a568bdfb74f35e2eadc2bcc9c6def516c8fe6c3e64b5f4db16e79f815cd208222447071a5da1b8aa7753867b1fa820844ffd5d982df7223; _gat=1'

    url = f'https://adventofcode.com/{year}/day/{day_number}/input'
    headers = {'user-agent': 'Mozilla/5.0', 'cookie': cookie}

    get_data = requests.get(url, headers=headers)
    data_returned = get_data.text.split('\n')
    data_dataframe = pd.DataFrame(columns=['data'], data=data_returned)

    return data_dataframe

