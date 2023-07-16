import requests
import os
import argparse
from urllib.parse import urlparse
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
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'.format(url=url)
    response = requests.get(url, headers=headers)  
    return response.ok    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('long_link', help='Длинное имя ссылки')
    url = parser.parse_args().long_link

    load_dotenv()
    token = os.getenv("BITLY_TOKEN")

    url_urllib = urlparse(url)
    url_minus_https = "{netloc}{path}{params}{query}{fragment}".format(netloc = url_urllib.netloc, path = url_urllib.path,
                                                                       params = url_urllib.params, query = url_urllib.query,
                                                                       fragment = url_urllib.fragment)

    if is_bitlink(token,url_minus_https):
        try:
            clicks_count = count_clicks(token, url_minus_https)
            print(clicks_count)
        except requests.exceptions.HTTPError:
            print("Вы неправильно ввели адрес! Запустите программу еще раз!") 
    else:
        try:
            bitlink = shorten_link(token,url)
            print('Битлинк', bitlink)
        except requests.exceptions.HTTPError:    
            print("Неправильно ввели адрес! Запустите программу еще раз!")    


if __name__ == '__main__':
    main()