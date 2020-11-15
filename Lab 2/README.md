### LAB
#### Хід роботи

1. За допомогою пакетного менеджера *PIP* інсталював pipenv та створив ізольоване середовище для *Python*.
```
pip install pipenv
pipenv --python 3.8 
pipenv shell
```
2. Встановив бібліотеки *requests* та *ntplib* у своєму середовищі.
```
pipenv install requests
pipenv install ntplib
```
3. Переконався що програма працює правильно.
```
python app.py
```
Результат:
```
========================================
Результат без параметрів: 
No URL passed to function
========================================
Результат з правильною URL: 
Time is:  10:32:21 PM
Date is:  15-11-2020
```
4. Встановив бібліотеку *pytest* та запустив тести, всі тести виконались успішно:
```
pipenv install pytest
pytest tests/tests.py
```
5. Дописав у програмі функцію, що перевіряє час доби на AM/PM та відповідно друкувати "Доброго дня/ночі". Також написав тест який перевіряє правильність роботи функції.
6. Перенаправив результат виконання функції та тестів у файл results.txt:
```
pipenv run pytest tests/tests.py >> results.txt
pipenv run python app.py append >> results.txt
```
7. Закомітив до репозиторію Makefile
-Створив Makefile
-Заповнив мейкфайл
-Запустив мейкфайл
