import pandas as pd
import json
import csv

def read_csv_file(path):
    """ считывание финансовых операций из CSV"""
    with open(path, encoding='UTF-8') as file:
        df = pd.read_csv(file, delimiter=';')
    result_dict = df.to_dict(orient='records')
    return result_dict

def read_excel_file(path):
    """ считывание финансовых операций из EXCEL"""
    df =  pd.read_excel(f'{path}')
    result_dict = df.to_dict(orient='records')
    return result_dict

if __name__ == '__main__':
    # print(read_csv_file('../transactions.csv'))
    print(read_excel_file('../transactions_excel.xlsx'))

