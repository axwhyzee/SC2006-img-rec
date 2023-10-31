"""
Test client for app
"""

import requests


def get_inference(url: str):
    r = requests.get(f'https://siah0026.pythonanywhere.com/inference', params={'url': url})
    print(r.json())


get_inference('https://images.data.gov.sg/api/traffic-images/2023/10/d715bc49-0faf-48ae-a3b1-b14aec539b0a.jpg')


