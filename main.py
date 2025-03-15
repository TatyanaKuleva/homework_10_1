
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date, filtr_by_category
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.decorators import log
from src.func_get_data_csv_excel import read_excel_file, read_csv_file
from src.utils import get_data_transaction, sum_one_transction

#
# transactions = (
#         [
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {
#                     "amount": "9824.07",
#                     "currency": {
#                         "name": "RUB",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702"
#             },
#             {
#                 "id": 142264268,
#                 "state": "EXECUTED",
#                 "date": "2019-04-04T23:20:05.206878",
#                 "operationAmount": {
#                     "amount": "79114.93",
#                     "currency": {
#                         "name": "",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 19708645243227258542",
#                 "to": "Счет 75651667383060284188"
#             },
#             {
#                 "id": 873106923,
#                 "state": "EXECUTED",
#                 "date": "2019-03-23T01:09:46.296404",
#                 "operationAmount": {
#                     "amount": "43318.34",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 44812258784861134719",
#                 "to": "Счет 74489636417521191160"
#             },
#             {
#                 "id": 895315941,
#                 "state": "EXECUTED",
#                 "date": "2018-08-19T04:27:37.904916",
#                 "operationAmount": {
#                     "amount": "56883.54",
#                     "currency": {
#                         "name": "RUB",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод с карты на карту",
#                 "from": "Visa Classic 6831982476737658",
#                 "to": "Visa Platinum 8990922113665229"
#             },
#             {
#                 "id": 594226727,
#                 "state": "CANCELED",
#                 "date": "2018-09-12T21:27:25.241689",
#                 "operationAmount": {
#                     "amount": "67314.70",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Visa Platinum 1246377376343588",
#                 "to": "Счет 14211924144426031657"
#             }
#         ]
#     )

def main():
    """Главная функция для работя приложения"""

    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print( f'Выберите необходимый пункт меню: \n 1. Получить информацию о транзакциях из JSON-файла \n 2. Получить '
           f'информацию о транзакциях из CSV-файла. \n 3. Получить информацию о транзакциях из XLSX-файла')

    user_input_file = int(input("Пользователь "))
    if user_input_file == 1:
        transaction = get_data_transaction('data/operations.json')
    elif user_input_file == 2:
        transaction = read_csv_file('data/transactions.csv')
    elif user_input_file == 3:
        transaction = read_excel_file('data/transactions_excel.xlsx')
    else:
        print("Выберите необходимый пункт меню")

    user_input_filtr = input('Введите статус, по которому необходимо выполнить фильтрацию. \n '
                             'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ')
    correct_status = ['EXECUTED', 'CANCELED', 'PENDING']

    if user_input_filtr.upper() in correct_status:
        print(f'Операции отфильтрованы по статусу {user_input_filtr}')
    else:







if __name__ == "__main__":
    print(main())

