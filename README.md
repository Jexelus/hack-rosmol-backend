# 1. Download repo

```bash
git clone --recursive https://github.com/Jexelus/hack-rosmol-frontend
```

# 2. Build
Увы но мы не даём в общий доступ сертификаты и api ключи от ботов и приложений, помните что вам необходимо будет: 
1. Привязать домен
2. Поменять настройки nginx 
3. Поместить в каталог ./nginx/certs сертификаты вашего домена
4. Для запука телеграмм бота вам так-же небходимо будет создать файл .env в папке ./tgbot с форматом ниже
5. Так-же в ``` ./docker-compose.yaml ``` небходимо будет пробросить порты в соответсвии с вашей системой, настройки проекта у вас не заведуться 

```bash
#.env file in ./tgbot
 API_KEY="YOUR_API_KEY" 
```

 vk работает на https, поэтому без этих шагов вы не сможете запустить проект, если не выполните этих шагов

# 3. Build front

```bash
cd ./frontend
npm start # дожидаемся конца установки и выходим
# далее запускаем две сессии терменала 
npm start # 1 session
npm tunnel # 2 session
```
В выводе из 2-ой сессии вы получите ссылку https для тунеля в вк, нужно будет вписать её в настройки вашего приложения в [https://dev.vk.com/ru/](https://dev.vk.com/ru/)

# 4. API DOCS
Документация по api будет доступна на вашем домене после деплоя проекта по адрессу [https://your-domain.ru/docs](https://your-domain.ru/docs)