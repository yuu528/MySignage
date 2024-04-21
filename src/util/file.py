import os
import requests

def download_tmp(url):
    if exists_tmp(url):
        return

    res = requests.get(url)

    with open(os.path.join(get_tmp_dir(), os.path.basename(url)), 'wb') as file:
        file.write(res.content)

    return res.text

def exists_tmp(url):
    return os.path.isfile(os.path.join(get_tmp_dir(), os.path.basename(url)))

def get_tmp_path(url):
    return os.path.join(get_tmp_dir(), os.path.basename(url))

def get_tmp_dir():
    tmp_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), os.pardir, os.pardir, 'tmp'
        )
    )

    if not os.path.isdir(tmp_dir):
        os.makedirs(tmp_dir)

    return tmp_dir
