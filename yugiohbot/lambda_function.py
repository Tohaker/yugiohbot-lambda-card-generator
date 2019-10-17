from card import *


def lambda_handler(event, context):
    return {'card_file': 'card.jpg'}


if __name__ == '__main__':
    print(lambda_handler({'title': 'test-title', 'text': 'test-text'}, None))
