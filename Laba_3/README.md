# LAB3

## Хід роботи


1. За допомогою *Django Framework* створив заготовку проекту та виніс всі створені файли на один рівень вище
```
pipenv run django-admin startproject my_site
    
        mv my_site/site_lab3/* my_site/
        mv my_site/manage.py ./
```
2. Переконався, що все встановилось правильно `pipenv run python manage.py runserver`:
```
    November 25, 2020 - 16:48:07
Django version 3.1.3, using settings 'my_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C
```
3. Створив потрібні папки та файли.
4. Перевірив, як працюють сторінки `127.0.0.1:8000` та `127.0.0.1:8000/health`:<br/>
```
You are at main page.

test
```		 
/////
	```
	date	"25/11/2020 16:49:11"
current_page	"http://127.0.0.1:8000/health/"
server_info	
0	"Linux"
1	"bodiq-VirtualBox"
2	"5.8.0-29-generic"
3	"#31-Ubuntu SMP Fri Nov 6 12:37:59 UTC 2020"
4	"x86_64"
client_info	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0" 
```
5. Створив файл monitoring.py та встановив бібліотеку:
```
pipenv install requests
```
6. Модифікував функцію `health`.
7. Дописав функціонал який виводить повідомлення про недоступність сайту у випадку якщо WEB сторінка недоступна.
8. Зробив так щоб програма `monitoring.py` запускалась раз в хвилину та працювала в бекграунді.
9. Cпростив роботу з пайтон середовищем через швидкий виклик довгих команд:
```
server = "python manage.py runserver"
monitoring = "python3 monitoring.py"
```

