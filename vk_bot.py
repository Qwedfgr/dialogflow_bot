import logging
import os
import random

import dotenv
import telegram
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

from df_utils import get_answer
import log_utils


dotenv.load_dotenv()
TOKEN_VK = os.environ["TOKEN_VK"]
CHAT_ID = os.environ["chat_id"]

logger = logging.getLogger("bot-logger")


def main():
    token_logger = os.environ["TOKEN_LOG"]
    logger_bot = telegram.Bot(token=token_logger)
    logger.setLevel(logging.INFO)
    logger.addHandler(log_utils.MyLogsHandler(logger_bot, CHAT_ID))
    try:
        run_vk_bot(TOKEN_VK)
    except Exception as error:
        logger.error(error, exc_info=True)


def dialog(event, vk_api):
    message, intent = get_answer(CHAT_ID, event.text, 'ru')
    if intent.is_fallback:
        return None

    vk_api.messages.send(
        user_id=event.user_id,
        message=message,
        random_id=random.randint(1, 1000)
    )


def run_vk_bot(token_vk):
    vk_session = VkApi(token=token_vk)
    vk_api = vk_session.get_api()
    logger.info('Бот для VK запущен')
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            dialog(event, vk_api)


if __name__ == '__main__':
    main()
