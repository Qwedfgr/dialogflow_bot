from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import df_utils

def run_tg_bot(TOKEN_TG):
    updater = Updater(TOKEN_TG)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, dialog))

    updater.start_polling()

    updater.idle()


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Здравствуйте!')


def dialog(bot, update):
    """Echo the user message."""
    text_message = df_utils.get_answer(PROJECT_ID, chat_id, [update.message.text], 'en-EN')
    update.message.reply_text(text_message)
