import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
# # Задание 2. Начало
# url = 'https://api-ssl.bitly.com/v4/user'
# headers = {
#     'Authorization': 'Bearer 20dd24d804932570aa455be564e3992affd45ea1'
# }
# response = requests.get(url, headers=headers)
# response.raise_for_status()
# print(response.text)
# # Задание 2. Конец

# # Задание 3. Начало
# url = 'https://api-ssl.bitly.com/v4/bitlinks'
# headers = {
#     'Authorization': 'Bearer 20dd24d804932570aa455be564e3992affd45ea1'
# }
# payload = {
#   "long_url": "http://dvmn.org"
# }
# response = requests.post(url, headers=headers, json=payload)
# response.raise_for_status()
# print(response.json())
# # Задание 4. Конец

# Задание 5. Начало
def shorten_link(my_token, url_my):
    headers = {
    'Authorization': 'Bearer ' + my_token
    }
    payload = {
    "long_url": url_my
    }
    url_btl = 'https://api-ssl.bitly.com/v4/bitlinks'
    try:
        response = requests.post(url_btl, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError:    
        return 400
    return response.json()['link']

def count_clicks(token, link):
    headers = {
    'Authorization': 'Bearer ' + token
    }
    payload = {
    "long_url": link
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'+link+'/clicks/summary'
    try:
        response = requests.get(url, headers=headers, params=payload)  
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError:
        return None

def is_bitlink(url):
    parsed = urlparse(url)
    if (parsed.netloc == "bit.ly") or (parsed.path[:6] == "bit.ly"):
        return True
    else:
        return False

def main():
    url_my = input()
    load_dotenv()
    token_my = os.getenv("token")

    # Задание 10. Начало
    if is_bitlink(url_my) == False:
        bitlink = shorten_link(token_my,url_my)
        if bitlink == 400:
            print("Неправильно ввели адрес! Запустите программу еще раз!")
        else:    
            print('Битлинк', bitlink)
    else:
        clicks_count = count_clicks(token_my, url_my)
        if clicks_count == None:
            print("Вы неправильно ввели адрес! Запустите программу еще раз!")        
        else:
            print(clicks_count)
    # Задание 10. Конец

    # # Задание 8. Начало
    # if is_bitlink(url_my) == False:
    #     try:
    #         bitlink = shorten_link(token_my,url_my)
    #         print('Битлинк', bitlink)
    #     except Exception:
    #         print("Запустите программу еще раз!")
    # else:
    #     clicks_count = count_clicks(token_my, url_my)
    #     if clicks_count == None:
    #         print("Запустите программу еще раз!")        
    #     else:
    #         print(clicks_count)
    # # Задание 8. Конец

    # # Задание 8. Начало
    # if is_bitlink(url_my) == False:
    #     try:
    #         bitlink = shorten_link(token_my,url_my)
    #         print('Битлинк', bitlink)
    #     except Exception:
    #         print("Запустите программу еще раз!")
    # else:
    #     clicks_count = count_clicks(token_my, url_my)
    #     if clicks_count == None:
    #         print("Запустите программу еще раз!")        
    #     else:
    #         print(clicks_count)
    # # Задание 8. Конец

    # Задание 6. Начало (Программа проверяет ссылку)
    # try:
    #     bitlink = shorten_link('20dd24d804932570aa455be564e3992affd45ea1',url_my)
    #     print('Битлинк', bitlink)
    # except Exception:
    #     print("Запустите программу еще раз!")
    # Задание 6. Конец
    
    # Задание 7. Начало (счетчик перехода по ссылкам)
    # clicks_count = count_clicks('20dd24d804932570aa455be564e3992affd45ea1', url_my)
    # if clicks_count == None:
    #     print("Запустите программу еще раз!")        
    # else:
    #     print(clicks_count)
    # Задание 7. Конец

if __name__ == '__main__':
    main()
# Задание 5. Конец