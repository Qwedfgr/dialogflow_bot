import logging
import os

import dotenv
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from df_utils import get_answer
import log_utils


logger = logging.getLogger("bot-logger")


def main():
    dotenv.load_dotenv()
    token_tg = os.environ["token_tg"]

    dotenv.load_dotenv()
    token_logger = os.environ["TOKEN_LOG"]
    chat_id = os.environ["chat_id"]
    logger_bot = telegram.Bot(token=token_logger)

    logger.setLevel(logging.INFO)
    logger.addHandler(log_utils.MyLogsHandler(logger_bot, chat_id))
    try:
        run_tg_bot(token_tg)
    except Exception as error:
        logger.error(error, exc_info=True)


def run_tg_bot(token_tg):
    updater = Updater(token_tg)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, dialog))

    logger.info('Бот для телеграма запущен')
    updater.start_polling()

    updater.idle()


def start(bot, update):
    update.message.reply_text('Здравствуйте!')


def dialog(bot, update):
    text_message, _ = get_answer(update.message.chat_id, [update.message.text], 'ru')
    update.message.reply_text(text_message)


if __name__ == '__main__':
    main()
