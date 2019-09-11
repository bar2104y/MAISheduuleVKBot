import time, sqlite3

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# 
from parse import parse

# Импорт конфигурации
from config import token, group_vk
from resourse import Classificator

# Подключение к БД
conn = sqlite3.connect("MAIShedule.db")
cursor = conn.cursor()

Controller = Classificator()

def main():
    # Инициализация бота
    vk_session = vk_api.VkApi(token=token)
    longpoll = VkBotLongPoll(vk_session, group_vk)
    vk = vk_session.get_api()

    # Прослушивание событий
    for event in longpoll.listen():
        #Из всех событий нас интересуют только новые сообщения
        if event.type == VkBotEventType.MESSAGE_NEW:
            # Проверяем запрос
            # Проверяем пользователя
            # Формируем данные
            # Отправляяем ответ
            mes, keyboard = Controller.thread(event.obj.text, event.obj.from_id)
            vk.messages.send(
                    peer_id=event.obj.from_id,
                    random_id=get_random_id(),
                    keyboard=keyboard,
                    message=mes )

while True:
    try:
        main()
    except Exception as e:
        print(e.__class__)