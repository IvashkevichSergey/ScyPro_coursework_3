import json
import datetime
import os

JSON_FILE_NAME = 'operations.json'
current_working_directory = os.path.dirname(os.path.dirname(__file__))
path_to_json = os.path.join(current_working_directory, JSON_FILE_NAME)


def load_data():
    """Функция получает данные из json файла, обрабатывает их, оставляя только непустые словари
    с операциями в состоянии EXECUTED и возвращает список последних 5 операций, отсортированных
    от новым к старым"""
    with open(path_to_json, encoding='utf-8') as f:
        data = json.load(f)
    data = [operation for operation in data if len(operation) and operation['state'] == 'EXECUTED']
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    return sorted_data[:5]


def print_formatted_date(date):
    """Функция принимает строку с датой и временем, возвращает отформатированную дату"""
    date = date[:10]
    formatted_date = datetime.date.fromisoformat(date)
    return formatted_date.strftime("%d.%m.%Y")


def print_operation_from_to(operation_from_to):
    """Функция обрабатывает данные по номеру карты/счёта отправителя и получателя для вывода на печать"""
    *count_type, count_number = operation_from_to.split()
    # Описываем различные варианты отображения для номера счёта либо номера карты
    if count_type[0].lower() == 'счет':
        count_number = '**' + count_number[-4:]
    else:
        count_number = count_number[:4] + ' ' + count_number[4:6] + '** **** ' + count_number[-4:]
    return f"{' '.join(count_type)} {count_number}"


def print_transaction_amount(operation_amount):
    """Функция возвращает сумму и валюту операции"""
    sum_of_transaction = operation_amount['operationAmount']['amount']
    transaction_currency = operation_amount['operationAmount']['currency']['name']
    return f'{sum_of_transaction} {transaction_currency}'


def print_transaction_info(transaction_data):
    """Выводит на печать данные по транзакции в требуемом виде"""
    # Получаем дату в необходимом формате
    date_to_print = print_formatted_date(transaction_data['date'])

    # Обрабатываем данные счёта отправителя и сохраняем в переменную
    try:
        operation_from = print_operation_from_to(transaction_data['from'])
    except KeyError:
        operation_from = '<Данные отправителя отсутствуют>'

    # Получаем данные счёта получателя
    operation_to = print_operation_from_to(transaction_data['to'])

    # Получаем данные о сумме транзакции
    operation_amount = print_transaction_amount(transaction_data)

    return f'{date_to_print} {transaction_data["description"]}\n' \
           f'{operation_from} -> {operation_to}\n' \
           f'{operation_amount}\n'
