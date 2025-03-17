import pandas as pd
import json
import csv

def read_csv_file(path):
    """ считывание финансовых операций из CSV"""
    df = pd.read_csv(path, delimiter=';')
    result_dict = df.to_dict(orient='records')
    return result_dict

def read_excel_file(path):
    """ считывание финансовых операций из EXCEL"""
    df =  pd.read_excel(path)
    result_dict = df.to_dict(orient='records')
    return result_dict



