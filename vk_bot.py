import random
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType


def echo(event, vk_api):
    vk_api.messages.send(
        user_id=event.user_id,
        message=event.text,
        random_id=random.randint(1, 1000)
    )


def run_vk_bot(token_vk):
    vk_session = VkApi(token=token_vk)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)