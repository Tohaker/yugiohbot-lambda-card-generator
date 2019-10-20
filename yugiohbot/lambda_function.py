import datetime
import logging
import os
import random

from card import neocardmaker as neo
from utils import *


def lambda_handler(event, context):
    logging.debug('Received event: ' + event)

    title = event['title']
    effect = event['text']
    logging.debug('Received title: ' + title)
    logging.debug('Received text: ' + effect)

    card_image = str(random.choice(csvutils.get_card_ids('resources/cards_api.csv'))) + '.jpg'
    s3utils.download_cropped_image_from_s3(card_image)
    card_image_path = os.path.abspath(card_image)
    logging.debug('Chosen image: ' + card_image + '. Full path: ' + card_image_path)

    rarity = ['common', 'rare', 'ultra', 'secret']
    template = ['Normal', 'Effect', 'Ritual', 'Fusion', 'Synchro', 'DarkSynchro', 'Xyz', 'Unity', 'Link',
                'Token', 'Spell', 'Trap', 'Skill']
    attribute = ['None', 'Dark', 'Divine', 'Earth', 'Fire', 'Light', 'Water', 'Wind', 'Spell', 'Trap']
    cardtype = ['Monster', 'Ritual', 'Fusion', 'Spell', 'Trap', 'Synchro', 'Xyz']

    card_rarity = random.choice(rarity)
    card_template = random.choice(template)
    card_attribute = random.choice(attribute)
    card_type = random.choice(cardtype)

    attack = str(int(round(random.randint(0, 7000), -2)))
    defense = str(int(round(random.randint(0, 7000), -2)))
    card_serial = str(random.randint(0, 9999999999))

    final_image_path = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%S") + '.jpg'

    logging.debug('rarity: ' + card_rarity)
    logging.debug('template: ' + card_template)
    logging.debug('attribute: ' + card_attribute)
    logging.debug('type: ' + card_type)
    logging.debug('attack : ' + attack)
    logging.debug('defense: ' + defense)
    logging.debug('serial: ' + card_serial)

    neo.create_card(name=title, rarity=card_rarity, template=card_template, attribute=card_attribute,
                    level=str(random.randint(0, 12)), picture=card_image_path, type=card_type,
                    effect=effect, atk=attack, defense=defense, creator='YuGiOh-Bot', year='2019',
                    serial=card_serial, filename=final_image_path)

    result = {'card_file': final_image_path}
    logging.debug(result)
    return result


if __name__ == '__main__':
    print(lambda_handler({'title': 'test-title', 'text': 'test-text'}, None))
