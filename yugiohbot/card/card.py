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


def fillInNeoCardMaker(**kwargs):
    url = 'https://yemachu.github.io/cardmaker/'
    url_args = ['name', 'rarity', 'template', 'attribute', 'level', 'picture', 'type', 'effect',
                'atk', 'defense', 'circulation', 'creator', 'year', 'serial', 'filename']

    driver = setupNeoCardMakerPage(url)
    cp = '© ' + kwargs.get('year') + ' ' + kwargs.get('creator')

    fillInNeoCardMakerTextBox(driver, 'Name', kwargs.get('name'))
    selectFromNeoCardMakerDropdown(driver, 'Rarity', kwargs.get('rarity'))
    selectFromNeoCardMakerDropdown(driver, 'Template', kwargs.get('template'))
    selectFromNeoCardMakerDropdown(driver, 'Attribute', kwargs.get('attribute'))
    fillInNeoCardMakerTextBox(driver, 'Level', kwargs.get('level'))
    uploadPhotoToNeoCardMaker(driver, kwargs.get('picture'))
    fillInNeoCardMakerTextBox(driver, 'Type', kwargs.get('type'))
    fillInNeoCardMakerTextArea(driver, 'Effect', kwargs.get('effect'))
    fillInNeoCardMakerTextBox(driver, 'Attack', kwargs.get('atk'))
    fillInNeoCardMakerTextBox(driver, 'Defense and/or Link', kwargs.get('defense'))
    fillInNeoCardMakerTextBox(driver, 'Serial number', kwargs.get('serial'))
    fillInNeoCardMakerTextBox(driver, 'Copyright', cp)

    downloadCardImageFromNeoCardMaker(driver, kwargs.get('filename'))
    driver.close()


def fillInNeoCardMakerTextBox(driver, name, value):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    textBox = driver.find_element(By.XPATH, '//label[text()=\"' + name + '\"]/input[1]')
    textBox.clear()
    textBox.send_keys(value)


def fillInNeoCardMakerTextArea(driver, name, value):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    textArea = driver.find_element(By.XPATH, '//label[text()=\"' + name + '\"]/textarea[1]')
    textArea.clear()
    textArea.send_keys(value)


def selectFromNeoCardMakerDropdown(driver, name, value):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    dropdown = Select(driver.find_element(By.XPATH, '//label[text()=\"' + name + '\"]/select[1]'))
    dropdown.select_by_value(value)


def uploadPhotoToNeoCardMaker(driver, filepath):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    driver.find_element(By.XPATH, '//label[text()="Image"]/input[2]').send_keys(filepath)
    driver.implicitly_wait(2)


def setupNeoCardMakerPage(url):
    driver = startWebdriver()
    driver.get(url)
    assert "Neo New card maker" in driver.title
    driver.implicitly_wait(1)
    button = driver.find_element(By.XPATH, '//button[text()="New"]')
    button.click()
    return driver

def startWebdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--')
    # chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"
    return webdriver.Chrome(chrome_options=chrome_options)


def downloadCardImageFromNeoCardMaker(driver, filename):
    assert "Neo New card maker" in driver.title  # First make sure we're still on the same page.
    canvas = driver.find_element(By.XPATH, '//canvas[1]')
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    canvas_png = base64.b64decode(canvas_base64)
    with open(filename, 'wb') as f:
        f.write(canvas_png)





if __name__ == '__main__':
    driver = setupNeoCardMakerPage('https://yemachu.github.io/cardmaker/')
    file = os.path.abspath("data/cropped/11.jpg")
    uploadPhotoToNeoCardMaker(driver, file)
    downloadCardImageFromNeoCardMaker(driver, 'ygo.png')
    driver.close()
