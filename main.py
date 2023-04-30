from utils import utils

if __name__ == '__main__':
    # По каждой из 5 транзакций выводим краткую информацию
    for transaction in utils.load_data():
        print(utils.print_transaction_info(transaction))
