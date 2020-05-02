import os
from dotenv import load_dotenv

from functools import partial

import redis

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler

from handlers.tg import (handle_new_question_request, handle_surrender, handle_stat_request,
                         handle_solution_attempt,
                         CHOOSING)

import logging

logger = logging.getLogger(__name__)


def start(bot, update):
    custom_keyboard = [['Новый вопрос', 'Сдаться'],
                       ['Моя статистика']]

    update.message.bot.send_message(chat_id=update.message.from_user.id,
                                    text='Привет! Я бот для викторин!',
                                    reply_markup=ReplyKeyboardMarkup(custom_keyboard)
                                    )
    return CHOOSING


def cancel(bot, update):
    return ConversationHandler.END


def help(bot, update):
    """Send a message when the command /help is issued."""

    text = 'Чтобы запустить бота, введите команду /start'
    update.message.reply_text(text)


def main():
    load_dotenv()
    token = os.environ['TG_TOKEN']
    encoding = os.environ.get('ENCODING', 'UTF-8')

    redis_db = redis.Redis(host=os.environ['REDIS_HOST'],
                           port=os.environ['REDIS_PORT'],
                           password=os.environ['REDIS_PASSWORD'],
                           db=0
                           )

    updater = Updater(token)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [RegexHandler('Новый вопрос',
                                    partial(handle_new_question_request, redis_db=redis_db, encoding=encoding)),
                       RegexHandler('Сдаться', partial(handle_surrender, redis_db=redis_db)),
                       RegexHandler('Моя статистика', partial(handle_stat_request, redis_db=redis_db)),

                       MessageHandler(Filters.text, partial(handle_solution_attempt, redis_db=redis_db))
                       ]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    dp.add_handler(CommandHandler('help', help))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
