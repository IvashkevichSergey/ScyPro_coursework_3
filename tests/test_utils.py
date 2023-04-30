from utils import utils

DATA_FOR_TEST = {
    "date": "2018-07-06T22:32:10.495465",
    "operationAmount": {
      "amount": "37160.27",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 4062745111784804",
    "to": "Maestro 8602249654751155"
  }


def test_load_data():
    assert type(utils.load_data()) == list
    assert type(utils.load_data()[0]) == dict
    assert len(utils.load_data()) == 5


def test_print_formatted_date():
    assert utils.print_formatted_date('2019-02-12T00:08:07.524972') == '12.02.2019'
    assert utils.print_formatted_date(DATA_FOR_TEST['date']) == '06.07.2018'


def test_print_operation_from_to():
    assert utils.print_operation_from_to('Счет 468783388932561475281') == 'Счет **5281'
    assert utils.print_operation_from_to(DATA_FOR_TEST['from']) == 'Visa Classic 4062 74** **** 4804'
    assert utils.print_operation_from_to(DATA_FOR_TEST['to']) == 'Maestro 8602 24** **** 1155'


def test_print_transaction_amount():
    assert utils.print_transaction_amount(DATA_FOR_TEST) == '37160.27 руб.'


def test_print_print_transaction_info():
    assert utils.print_transaction_info(DATA_FOR_TEST) == '06.07.2018 Перевод с карты на карту\n' \
                                                           'Visa Classic 4062 74** **** 4804 -> ' \
                                                           'Maestro 8602 24** **** 1155\n' \
                                                           '37160.27 руб.\n'
