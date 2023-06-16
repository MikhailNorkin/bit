import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

def shorten_link(token, long_url):
    headers = {
    'Authorization': 'Bearer {token}'.format(token=token)
    }
    payload = {
    "long_url": long_url
    }
    bytly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(bytly_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']

def count_clicks(token, link):
    headers = {
    'Authorization': 'Bearer {token}'.format(token=token)
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'.format(link=link)
    response = requests.get(url, headers=headers)  
    response.raise_for_status()
    return response.text

def is_bitlink(token,url):
    headers = {
    'Authorization': 'Bearer {token}'.format(token=token)
    }
    payload = {
    "long_url": url
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'.format(url=url)
    response = requests.get(url, headers=headers, params=payload)  
    return response.ok    

def main():
    url = input()
    load_dotenv()
    token = os.getenv("TOKEN_BIT")

    if not is_bitlink(token,url):
        try:
            bitlink = shorten_link(token,url)
            print('Битлинк', bitlink)
        except requests.exceptions.HTTPError:    
            print("Неправильно ввели адрес! Запустите программу еще раз!")
    else:
        try:
            clicks_count = count_clicks(token, url)
            print(clicks_count)
        except requests.exceptions.HTTPError:
            print("Вы неправильно ввели адрес! Запустите программу еще раз!")        

if __name__ == '__main__':
    main()