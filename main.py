from utils import utils

if __name__ == '__main__':
    for transaction in utils.load_data():
        print(utils.print_transaction_info(transaction))
