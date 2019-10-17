import shutil
import urllib.parse

import requests


def construct_request(**kwargs):
    base_url = "https://www.yugiohcardmaker.net/ycmaker/createcard.php?"
    url_args = ['name', 'cardtype', 'trapmagictype', 'subtype', 'attribute', 'level', 'rarity', 'picture',
                'circulation', 'set1', 'set2', 'type', 'carddescription', 'atk', 'def', 'creator', 'year', 'serial']
    url_dict = {}

    for arg in url_args:
        # index = url_args.index(arg)
        kw = kwargs.get(arg) if kwargs.get(arg) is not None else ""  # Check if the Key Word argument has been supplied.
        url_dict[arg] = kw  # Build up a dictionary of all the arguments.

    base_url += urllib.parse.urlencode(url_dict)
    return base_url


def download_image(url, path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
