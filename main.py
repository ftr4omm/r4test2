import time
import requests
import pandas as pd


def get_cryptopia_json():
    url_curr = 'https://www.cryptopia.co.nz/api/GetCurrencies'
    resp = requests.get(url_curr)
    json = resp.json()
    return json


def main():
    while True:
        datas = get_cryptopia_json()
        df_columns = ['Id', 'Name', 'Symbol', 'Algorithm', ]
        df = pd.DataFrame(columns=df_columns)
        exclude_list = ['SHA256', 'None', 'POS', 'Scrypt', 'Other']

        for data in datas['Data']:
            coin_data = [int(data['Id']), data['Name'], data['Symbol'], data['Algorithm']]
            df.loc[len(df)] = coin_data

        df = df.set_index('Id')
        df = df.sort_index()
        print('Total Active coins: ', len(df))
        print(df.tail(10))
        time.sleep(60)


if __name__ == "__main__":
    main()
