# Сокращение ссылок
Программа позволяет сократить длину ссылок через сервис bit.ly

# Как установить
Скрипт совместим с Phyton с библиотеками requests и python-dotenv<br/> 
Зависимости находятся в файле "requirements.txt"<br/>
Используйте `pip` (или `pip3`, если есть конфликт с python2) для установки зависимостей:<br/>
```
pip install -r requirements.txt
```
Рекомендуется использовать virtualenv/venv для изоляции проекта

# Переменные окружения
Библиотека python-dotenv - позволяет загружать переменные окружения из файла .env в корневом каталоге приложения.<br/>
В файле .env храниться токен BITLY_TOKEN, который позволяет работать с сервисом bit.ly

# Цель проекта
Сокращение длины ссылок, а также проверка корректности ввода ссылок.

# Работа программы
После запуска необходимо ввести имя ссылки и нажать Enter. Далее программа проверит корректность ввода ссылки и при удачной проверке выдаст сокращенный вариант,
который будет получен через сервис bit.ly. В случае некорректного ввода программа выдаст ошибку.

# Пример работы программы
Если мы хотим, допустим получить коротку ссылку на сайт https://www.google.ru/, то необхоимо ввести команду: 
```
python3 main.py https://www.google.ru/
```
Если ссылка введена верно, то программа выведет ее короткую версию в следующем формате:<br/>
```
Битлинк https://bit.ly/3NyCTLS
```