# Raid-Bot-VK
Рейд бот для флуда в беседах. Поддерживается добавление нескольких ботов (количество упирается только в возможности вашего пк). Размещение - группа.
## Настройка
Устанавливаем недостающие библиотеки из файла requirements.txt

Заполняем поля файла accounts.json:
```
"pod_token" = "" - токен для приглашения ботов в беседу через скрипт, если вы сами будете приглашать ботов в беседу, то он не нужен
"group_token" = "" - токен группы с которой будет происходить рейд
"group_id": - айди группы с которой будет происходить рейд
```
Переходим [сюда](https://oauth.vk.com/authorize?client_id=6441755&scope=262144&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1) для получения "pod_token", нажимаем Разрешить. В адресной строке, все что между token= и & копируем и вставляем в "pod_token"

Для получения токена группы переходим в нужную группу:
```
Управление -> Настройки -> Работа с API -> Создать ключ -> Выставляем галочки и создаем
```
Для получения айди группы переходим в нужную группу:
```
Управление -> Настройки -> Адрес сообщества -> Номер сообщества -> club*цифры* -> Копируем только цифры
```
В файле RaidBot.py в 54 строке копируем все что в кавычках, создаем в своей группе пост и вставляем скропированный текст. Нажимаем на дату поста и копируем из адресной строки все что полсе w=, пример - wall-196079784_14. Вставляем это в 55 строку в поле attachment
## Компиляция
Чтобы собрать все в .exe файл используем команду:
```
pyinstaller --onefile RaidBot.py 
```
Чтобы все работало - помещаем .exe файл и accounts.json в одну папку
