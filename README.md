# Quiz-bot (бот-викторина) для VK и Telegram


В данном боте реализованы следующие функции:
* кнопочное меню
* анализ ответов пользователей
* хранение статистики в базе данных Redis

Пример для Telegram:  
![Картинка][image1]  

Пример для ВКонтакте:  
![Картинка][image2]


### Заведите базу данных Redis

База данных нужна для хранения статистики,
а так же для хранения информации о вопросах и ответах  

* https://redislabs.com/  
Вы получите адрес базы данных вида:  
`redis-13965.f18.us-east-4-9.wc1.cloud.redislabs.com`,   
его порт вида: `16635`,  и пароль.



### Как запустить ботов на Heroku

1. Зарегистрируйте приложение на [Heroku]
2. В созданном приложении во вкладке `Deploy`
привяжите данный github-репозиторий в `Deployment method`
и нажмите `Deploy Branch` внизу страницы
3. Во вкладке `Settings` подключите Python-пакет (Add buildpack):
    * `heroku/python`

3. Во вкладке `Settings` заполните переменные:
   ```
   TG_TOKEN=1234abcd   
   VK_TOKEN=1234abcd
   
   REDIS_HOST=redis-12345.a01.ab-abcd-0-1.ab0.cloud.redislabs.com  
   REDIS_PORT=12345
   REDIS_PASSWORD=1234abcd
   ```
4. Во вкладке `Resources` запустите сервер  
   Можно запустить сразу двух ботов


### Как запустить на своей машине

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

1. Создайте в корневой папке файл ```.env``` и пропишите в нем переменные следующим образом:  
    ```
   TG_TOKEN=12345abcde   
   VK_TOKEN=12345abcde
   
   REDIS_HOST=redis-12345.a01.ab-abcd-0-1.ab0.cloud.redislabs.com  
   REDIS_PORT=12345
   REDIS_PASSWORD=12345abcde
    ```

2. Запустите ботов: ```python tg_bot.py.py``` или ```python vk_bot.py.py```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков 
[dvmn.org](https://dvmn.org/modules/chat-bots/lesson/quiz-bot/).

[Heroku]: https://id.heroku.com/login "Heroku"


[image1]: https://dvmn.org/filer/canonical/1569215494/324/
[image2]: https://dvmn.org/filer/canonical/1569215498/325/
