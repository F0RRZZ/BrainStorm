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

Описание:
1. ALLOWED_HOSTS - список разрешенных хостов
2. DEBUG - режим отладки
3. EMAIL_ADDRESS - адрес электронной почты, с которой будут приходить письма польщователям
4. EMAIL_PASSWORD - адрес от электронной почты
5. GITHUB_CLIENT_ID - client id приложения в гитхабе
6. GITHUB_SECRET_KEY - секретный ключ приложения в гитхабе
7. SECRET_KEY - секретный ключ
8. USERS_AUTOACTIVATE - режим автоактивации пользователей (отключение подтверждения аккаунта)


Для получения client_id и secret key вам нужно зарегистрировать свое приложение на сайте GitHub.
1. Войдите в свой аккаунт на сайте GitHub.
2. Перейдите на страницу настроек приложений: https://github.com/settings/applications/new
3. Введите название вашего приложения в поле "Application name".
4. Введите домен вашего сайта в поле "Homepage URL".
5. Введите URL-адрес, на который GitHub будет перенаправлять пользователей после успешной аутентификации, в поле "Authorization callback URL".
6. Нажмите на кнопку "Register application".
7. Вам будет предоставлен client_id и secret key.

---

5. Создайте базу данных
Создание с помощью миграций
    
| Windows                               | Linux/MacOS                            |
|---------------------------------------|----------------------------------------|
| ```python manage.py makemigrations``` | ```python3 manage.py makemigrations``` |
| ```python manage.py migrate```        | ```python3 manage.py migrate```        |

Далее нужно создать аккаунт суперпользователя

| Windows                                | Linux/MacOS                             |
|----------------------------------------|-----------------------------------------|
| ```python manage.py createsuperuser``` | ```python3 manage.py createsuperuser``` |

6. Сгенерируйте файлы для перевода

| Windows                                | Linux/MacOS                                |
|----------------------------------------|--------------------------------------------|
| ```python manage.py compilemessages``` | ```python3 manage.py compilemessages```|

7. Установить сервер redis

| Windows                      | Linux/MacOS                                |
|------------------------------|--------------------------------------------|
| ```https://clck.ru/34A34T``` | ```sudo docker run -d -p 6379:6379 redis```|


8. Запустите сервер

| Windows                          | Linux/MacOS                       |
|----------------------------------|-----------------------------------|
| ```python manage.py runserver``` | ```python3 manage.py runserver``` |


9. Запустите worker(в отдельном терминале)

```shell
celery -A brainstorm worker -l info
```

10. Запустите beat(в отдельном терминале)

```shell
celery -A brainstorm beat -l info
```

Далее перейдите по ссылке 
```
http://127.0.0.1:8000
```
