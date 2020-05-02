import os
from dotenv import load_dotenv

import redis

from vk_api import VkApi
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

from handlers.vk import hadle_message


def main():
    load_dotenv()
    token = os.environ['VK_TOKEN']

    redis_db = redis.Redis(host=os.environ['REDIS_HOST'],
                           port=os.environ['REDIS_PORT'],
                           password=os.environ['REDIS_PASSWORD'],
                           db=0
                           )

    vk_session = VkApi(token=token)
    vk_api = vk_session.get_api()

    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Новый вопрос', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Сдаться', color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()

    keyboard.add_button('Моя статистика', color=VkKeyboardColor.DEFAULT)

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            message = hadle_message(event.text, event.user_id, redis_db)

            vk_api.messages.send(peer_id=event.user_id,
                                 random_id=get_random_id(),
                                 keyboard=keyboard.get_keyboard(),
                                 message=message)


if __name__ == "__main__":
    main()
