import logging
import os
import requests
import time

from settings import API_URL, DOWNLOAD_FOLDER

logger = logging.getLogger()


def download(url: str):
    """
    Download image at specified URL

    Params
    ------
    url : str
        URL of image to download
    """
    img_data = requests.get(url).content
    logger.info(f'Downloading: {url}')

    try:
        if not os.path.exists(DOWNLOAD_FOLDER):
            os.mkdir(DOWNLOAD_FOLDER)

        with open(f'{DOWNLOAD_FOLDER}/{url.split("/")[-1]}', 'wb') as handler:
            handler.write(img_data)
    except Exception as e:
        logger.error(e)


def loop_download(n: int = 5):
    """
    Continously query the taffic camera API & download images every min
    """
    k = 1
    while 1:
        logger.info('New query cycle')
        r = requests.get(API_URL)
        items = r.json().get('items', [])
        
        for item in items:
            for cam in item.get('cameras', []):
                url = cam.get('image')
                if url:
                    download(url)
                    k += 1
                    if k > n:
                        return
        time.sleep(60)


if __name__ == '__main__':
    loop_download(3)