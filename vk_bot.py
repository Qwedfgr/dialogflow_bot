import random
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
import df_utils


def dialog(event, vk_api, PROJECT_ID):
    vk_api.messages.send(
        user_id=event.user_id,
        message= df_utils.get_answer(PROJECT_ID, chat_id, event.text, 'en-EN'),
        random_id=random.randint(1, 1000)
    )


def run_vk_bot(token_vk, PROJECT_ID):
    vk_session = VkApi(token=token_vk)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            dialog(event, vk_api, PROJECT_ID)