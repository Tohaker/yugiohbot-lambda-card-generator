# We can generate a card image using the following API:
# https://www.yugiohcardmaker.net/ycmaker/createcard.php?name=&cardtype=Monster&subtype=normal&attribute=Light&level=1
# &rarity=Common&picture=&circulation=&set1=&set2=&type=&carddescription=&atk=&def=&creator=&year=2019&serial=

# https://www.yugiohcardmaker.net/ycmaker/createcard.php?name=&cardtype=Spell&trapmagictype=Quick-Play&rarity=Common
# &picture=&circulation=&set1=&set2=&carddescription=&creator=&year=2019&serial=

import base64
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def create_card(**kwargs):
    url = 'https://yemachu.github.io/cardmaker/'

    driver = setup_web_driver(url)
    cp = '© ' + kwargs.get('year') + ' ' + kwargs.get('creator')

    fill_text_box(driver, 'Name', kwargs.get('name'))
    select_from_drop_down(driver, 'Rarity', kwargs.get('rarity'))
    select_from_drop_down(driver, 'Template', kwargs.get('template'))
    select_from_drop_down(driver, 'Attribute', kwargs.get('attribute'))
    fill_text_box(driver, 'Level', kwargs.get('level'))
    upload_card_image(driver, kwargs.get('picture'))
    fill_text_box(driver, 'Type', kwargs.get('type'))
    fill_text_area(driver, 'Effect', kwargs.get('effect'))
    fill_text_box(driver, 'Attack', kwargs.get('atk'))
    fill_text_box(driver, 'Defense and/or Link', kwargs.get('defense'))
    fill_text_box(driver, 'Serial number', kwargs.get('serial'))
    fill_text_box(driver, 'Copyright', cp)

    download_card_image(driver, kwargs.get('filename'))
    driver.close()


def fill_text_box(driver, name, value):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    text_box = driver.find_element(By.XPATH, '//label[text()=\"' + name + '\"]/input[1]')
    text_box.clear()
    text_box.send_keys(value)


def fill_text_area(driver, name, value):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    text_area = driver.find_element(By.XPATH, '//label[text()=\"' + name + '\"]/textarea[1]')
    text_area.clear()
    text_area.send_keys(value)


def select_from_drop_down(driver, name, value):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    drop_down = Select(driver.find_element(By.XPATH, '//label[text()=\"' + name + '\"]/select[1]'))
    drop_down.select_by_value(value)


def upload_card_image(driver, filepath):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    driver.find_element(By.XPATH, '//label[text()="Image"]/input[2]').send_keys(filepath)
    driver.implicitly_wait(2)


def setup_web_driver(url):
    driver = get_web_driver()
    driver.get(url)
    assert "Neo New card maker" in driver.title
    driver.implicitly_wait(1)
    button = driver.find_element(By.XPATH, '//button[text()="New"]')
    button.click()
    return driver


def get_web_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--')
    # chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"
    return webdriver.Chrome(chrome_options=chrome_options)


def download_card_image(driver, filename):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    canvas = driver.find_element(By.XPATH, '//canvas[1]')
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    canvas_png = base64.b64decode(canvas_base64)
    with open(filename, 'wb') as f:
        f.write(canvas_png)


if __name__ == '__main__':
    testdriver = get_web_driver('https://yemachu.github.io/cardmaker/')
    file = os.path.abspath("data/cropped/11.jpg")
    upload_card_image(testdriver, file)
    download_card_image(testdriver, 'ygo.png')
    testdriver.close()
