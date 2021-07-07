#!/usr/bin/env python3
import urllib.request
import re
import os

root_dir = os.path.dirname(__file__)

bing_index_url = 'https://www.bing.com/'

def main():
    print('start fetching...')
    page_src = urllib.request.urlopen(bing_index_url).read()

    href_m = re.search(r"""<link id="bgLink".+?href="(.+?)".+?>""", str(page_src))
    if href_m is None:
        return

    href = href_m.group(1)
    print('href', href)

    image_name_m = re.search(r"/th\?id=(.+?)&", href)
    image_name = image_name_m.group(1)
    print('image_name', image_name)

    image_url = '{}{}'.format(bing_index_url, href)
    urllib.request.urlretrieve(image_url, os.path.join(root_dir, 'images', image_name))

main()