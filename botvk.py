#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vk.com bot for groups and communities

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
import time

token = "insert************YoUr************ToKeN***********Grop****"
vk_session = vk_api.VkApi(token=token)
response=True
str(response)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

#Проверка сообщений и преобразование в нижний регистор полученные сообщения.
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        response = event.text.lower()
        response = event.text.casefold()
        if event.from_user and not (event.from_me):
            response = str(response)

#Начало(При нажатии кнопкии начать.При написании в сообщения слова "Начать" )
            if response == "начать":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Здравствуйте! Вас приветствует электронный помощник ', 'random_id': 0})
                time.sleep(1)
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Если у вас имеются вопросы, в скором времени мы на них ответим. Пока вы ожидаете, я помогу вам ускорить этот процесс и получить ответ гораздо быстрее!', 'random_id': 0})
                time.sleep(3)
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Если Ваш ответ «Да», выберите один из вариантов цифрой и отправьте в сообщения сообщества. \n 1) Мне необходимо подобрать план питания. \n 2) Мне нужна программа тренировок.','random_id': 0})

#Ответы
            if response == "1":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Для начала вам необходимо заполнить нашу анкету.', 'random_id': 0})

            if response == "2":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Для начала вам необходимо заполнить нашу анкету. https://vk.com/sushitelo?w=app5619682_-29551471', 'random_id': 0})

#Общение(Online)
            if response == "привет":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Здравствуйте', 'random_id': random.randint(1,1000)})

            if response == "пока":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'До скорой встречи', 'random_id': random.randint(1,1000)})

            if response == "как дела":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Неплохо, а у вас?', 'random_id': random.randint(1,1000)})

# Отправка админу оповещения. Необходимо убирать знаки (#id) ниже и написать (id) в виде цифр. того человека кому посылать оповещения о новых сообщениях группы. Дополнительно и не обязательно.
            else:
                xxx = random.randrange(99999)
                ran3 = 'В сообществе Сушка Тела | Shredded body новое сообщение #' + str(xxx) + ''
                vk_session.method('messages.send', {'user_id': 502892154, 'message': ran3, 'random_id': random.randint(1,1000)})

# Пишите мне в вк подскажу как поставить на бесплатный хостинг,что бы бот работал при выключенном компьютере. https://vk.com/id246536486
