<table>
  <tr>
    <td>
      <img src="assets/logo.jpg" alt="logo" width="150"/>
    </td>
    <td>
      <h1 style="padding-bottom: 40px;">Brainstorm</h1>
    </td>
  </tr>
</table>
### Установка и запуск

Для того, чтобы проделать следующие шаги на Windows, установите [Git Bash](https://gitforwindows.org/)

1. Склонируйте репозиторий

```shell
git clone https://github.com/F0RRZZ/BrainStorm.git
```
2. Создайте и активируйте venv

| Windows                            | Linux/MacOS                    |
|------------------------------------|--------------------------------|
| ```cd BrainStorm```                | ```cd Brainstorm```            |
| ```python -m venv venv```          | ```python3 -m venv venv```     |
| ```source venv/Scripts/activate``` | ```source venv/bin/activate``` |

3. Установите зависимости

* Основные зависимости

| Windows                                    | Linux/MacOS                                  |
|--------------------------------------------|----------------------------------------------|
| ```pip install -r requirements/prod.txt``` | ```pip3 install -r requirements/prod.txt```  |

*Зависимости для разработки

| Windows                                   | Linux/MacOS                                |
|-------------------------------------------|--------------------------------------------|
| ```pip install -r requirements/dev.txt``` | ```pip3 install -r requirements/dev.txt``` |

*Зависимости для тестирования

| Windows                                    | Linux/MacOS                                 |
|--------------------------------------------|---------------------------------------------|
| ```pip install -r requirements/test.txt``` | ```pip3 install -r requirements/test.txt``` |

4. Устанавите переменные окружения

```shell
cd brainstorm
```
```shell
cp .env-example .env
```

5. Создайте базу данных
* Первый способ. Создание с помощью миграций
    
| Windows                               | Linux/MacOS                            |
|---------------------------------------|----------------------------------------|
| ```python manage.py makemigrations``` | ```python3 manage.py makemigrations``` |
| ```python manage.py migrate```        | ```python3 manage.py migrate```        |

Далее нужно создать аккаунт суперпользователя

| Windows                                | Linux/MacOS                             |
|----------------------------------------|-----------------------------------------|
| ```python manage.py createsuperuser``` | ```python3 manage.py createsuperuser``` |

* Второй способ. Использование готовой базы данных

```shell
cp db_example.sqlite3 db.sqlite3
```

Так же можно подгрузить тестовые данные из фикстуры

| Windows                                   | Linux/MacOS                                |
|-------------------------------------------|--------------------------------------------|
| ```python manage.py loaddata data.json``` | ```python3 manage.py loaddata data.json``` |

6. Запустите сервер

| Windows                          | Linux/MacOS                       |
|----------------------------------|-----------------------------------|
| ```python manage.py runserver``` | ```python3 manage.py runserver``` |

Далее перейдите по ссылке 
```
http://127.0.0.1:8000
```
