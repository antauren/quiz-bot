import handlers.quiz as handler

CHOOSING = 1


def add_tg_prefix(id):
    return 'tg_{}'.format(id)


def handle_surrender(bot, update, redis_db):
    tg_user_id = add_tg_prefix(update.message.from_user.id)

    message = handler.handle_surrender(tg_user_id, redis_db)

    update.message.reply_text(message)

    return CHOOSING


def handle_stat_request(bot, update, redis_db):
    tg_user_id = add_tg_prefix(update.message.from_user.id)

    message = handler.handle_stat_request(tg_user_id, redis_db)

    update.message.reply_text(message)

    return CHOOSING


def handle_new_question_request(bot, update, redis_db, encoding):
    tg_user_id = add_tg_prefix(update.message.from_user.id)

    message = handler.handle_new_question_request(tg_user_id, redis_db, encoding)

    update.message.reply_text(message)

    return CHOOSING


def handle_solution_attempt(bot, update, redis_db):
    tg_user_id = add_tg_prefix(update.message.from_user.id)

    message = handler.handle_solution_attempt(update.message.text, tg_user_id, redis_db)

    update.message.reply_text(message)

    return CHOOSING
