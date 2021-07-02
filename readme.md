# VK-Raid-Bot

Рейд бот вк для флуда в беседах. Поддерживается добавление нескольких ботов одновременно (количество упирается только в возможности вашего пк). Размещение - группа.

## Настройка vk_api бота

Устанавливаем недостающие библиотеки из файла requirements.txt

Заполняем поля файла **accounts.json**:
| Поле                   | Описание                                                                                                         |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| pod_token              | Токен для приглашения ботов в беседу через скрипт, если вы сами будете приглашать ботов в беседу, то он не нужен |
| group_token            | Токен группы с которой будет происходить рейд                                                                    |
| group_id               | Айди группы с которой будет происходить рейд                                                                     |

Переходим [сюда](https://oauth.vk.com/authorize?client_id=6441755&scope=262144&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1) для получения "pod_token", нажимаем Разрешить. В адресной строке, все что между token= и & копируем и вставляем в "pod_token"

Для получения токена группы переходим в нужную группу:

```
-> Управление
-> Настройки
-> Работа с API
-> Создать ключ 
-> Выставляем галочки и создаем
```

Для получения айди группы переходим в нужную группу:

```
-> Управление
-> Настройки
-> Адрес сообщества
-> Номер сообщества
-> club*цифры* 
-> Копируем только цифры
```

Переходим [https://vk.com/wall-196079784_129](сюда), копируем текст, создаем в своей группе пост и вставляем скропированный текст. Нажимаем на дату поста и копируем из адресной строки все что полсе w=, пример - wall-196079784_14. Вставляем это в 61 строку в поле attachment

Также нужно настроить Long Poll API для бота:

```
-> Управление
-> Настройки
-> Работа с API
-> Long Poll API 
-> Long Poll API: Включено + Версия API: 5.92
-> Типы событий -> Выставляем галочки
```

И последний шаг:

```
-> Управление
-> Сообщения
-> Сообщения сообщества: Включены
-> Настройки для бота
-> Возможности ботов: Включены
-> Разрешать добавлять сообщество в беседы - ставим галочку
```

## Настройка vkbottle бота

Устанавливаем недостающие библиотеки из файла requirements.txt

Заполняем поля файла **config.py**:

```
TOKENS = [
  'токен от группы 1',
  'токен от группы 2',
  'токен от группы 3 и так далее'
]
```

Для получения токена группы переходим в нужную группу:

```
-> Управление 
-> Настройки
-> Работа с API
-> Создать ключ
-> Выставляем галочки и создаем
```

Также нужно настроить Long Poll API для бота:

```
-> Управление
-> Настройки
-> Работа с API
-> Long Poll API
-> Long Poll API: Включено + Версия API: самая новая
-> Типы событий -> Выставляем галочки
```

И последний шаг:

```
-> Управление
-> Сообщения
-> Сообщения сообщества: Включены
-> Настройки для бота
-> Возможности ботов: Включены
-> Разрешать добавлять сообщество в беседы - ставим галочку
```

## Запаковка в .ехе

Чтобы собрать все в .exe файл используем команду:

```
pyinstaller --onefile RaidBot.py
```

Чтобы все работало - помещаем .exe файл и accounts.json в одну папку
