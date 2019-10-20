from card import neocardmaker as neo
import logging


def lambda_handler(event, context):
    logging.debug('Received event: ' + event)

    title = event['title']
    effect = event['text']
    logging.debug('Received title: ' + title)
    logging.debug('Received text: ' + effect)

    neo.create_card()


    return {'card_file': 'card.jpg'}


if __name__ == '__main__':
    print(lambda_handler({'title': 'test-title', 'text': 'test-text'}, None))
