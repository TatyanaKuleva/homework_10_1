import pandas as pd
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date, filtr_by_category, filtr_by_data_in_string
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.decorators import log
from src.func_get_data_csv_excel import read_excel_file, read_csv_file
from src.utils import get_data_transaction, sum_one_transction, filtr_rub_transction

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


    correct_status = ['EXECUTED', 'CANCELED', 'PENDING']


    while True:
        user_input_status = input('Введите статус, по которому необходимо выполнить фильтрацию. \n '
                                  'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ').upper()
        if user_input_status in correct_status:
            break
        print(f'Статус операции {user_input_status} недоступен.')

    filtr_transacton_status = filter_by_state(transaction, user_input_status)

    user_input_sort_date = input('Отсортировать операции по дате? Да/Нет ').lower()

    if user_input_sort_date =='да':
        filtr_transacton_status_sort_date = sort_by_date(filtr_transacton_status)
    elif user_input_sort_date =='нет':
        filtr_transacton_status_sort_date = filtr_transacton_status

    user_input_sort_date_order = input('Отсортировать по возрастанию или по убыванию? ').lower()
    if user_input_sort_date_order =='по возрастанию':
        filtr_transacton_status_sort_date_order =sort_by_date(filtr_transacton_status_sort_date, False)
    elif user_input_sort_date_order =='по убыванию':
        filtr_transacton_status_sort_date_order = sort_by_date(filtr_transacton_status_sort_date)

    user_input_filtr_rub = input('Выводить только рублевые тразакции? Да/Нет? ').lower()
    if user_input_filtr_rub == 'да':
        filtr_transacton_status_rub = filtr_rub_transction(filtr_transacton_status_sort_date_order)
    elif user_input_filtr_rub == 'нет':
        filtr_transacton_status_rub = filtr_transacton_status_sort_date_order

    user_input_filtr_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет ').lower()
    if user_input_filtr_word == 'да':
        user_input_word_for_filtr = input('Введите слово для фильтрации ')
        filtr_transacton_status_word = filtr_by_data_in_string(filtr_transacton_status_rub, user_input_word_for_filtr)
    elif user_input_filtr_word == 'нет':
        filtr_transacton_status_word = filtr_transacton_status_rub

    if len(filtr_transacton_status_word)>1:
        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(filtr_transacton_status_word)}')
        for item in filtr_transacton_status_word:
            if 'operationAmount' in item:
                if item['description'] == 'Открытие вклада':
                    print(f'{get_date(item['date'])} {item['description']}')
                    print(f'{mask_account_card(item['to'])}')
                    print(f'Сумма {(item['operationAmount']['amount'])}.{(item['operationAmount']['currency']['name'])}')
                else:
                    print(f'{get_date(item['date'])} {item['description']}')
                    print(f'{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}')
                    print(f'Сумма {(item['operationAmount']['amount'])}.{(item['operationAmount']['currency']['name'])}')
            else:
                if item['description'] == 'Открытие вклада':
                    print(f'{get_date(item['date'])} {item['description']}')
                    print(f'{mask_account_card(item['to'])}')
                    print(f'Сумма {(item['amount'])}.{(item['currency_code'])}')
                else:
                    print(f'{get_date(item['date'])} {item['description']}')
                    print(f'{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}')
                    print(f'Сумма {(item['amount'])}.{(item['currency_code'])}')
    else:
        print('Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')






    # return filtr_transacton_status_word





if __name__ == "__main__":
    print(main())


