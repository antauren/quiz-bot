import handlers.quiz as handler

CHOOSING = 1


def handle_surrender(bot, update, redis_db):
    message = handler.handle_surrender(update.message.from_user.id, redis_db)

    update.message.reply_text(message)

    return CHOOSING


def handle_stat_request(bot, update, redis_db):
    message = handler.handle_stat_request(update.message.from_user.id, redis_db)

    update.message.reply_text(message)

    return CHOOSING


def handle_new_question_request(bot, update, redis_db):
    message = handler.handle_new_question_request(update.message.from_user.id, redis_db)

    update.message.reply_text(message)

    return CHOOSING


def handle_solution_attempt(bot, update, redis_db):
    message = handler.handle_solution_attempt(update.message.text, update.message.from_user.id, redis_db)

    update.message.reply_text(message)

    return CHOOSING
